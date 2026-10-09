#!/usr/bin/env bash
# Run COMMAND against a local Wiretap mock of SPEC: wiretap.sh SPEC COMMAND [ARGS...]
# COMMAND gets WIRETAP_URL. Wiretap's log and report go to VALIDATION_ARTIFACTS.
# Fails if COMMAND fails or Wiretap reports any violation besides the canary.
# Copied unchanged into each UpCloud SDK repository; wiretap and jq come from mise.
set -euo pipefail

[ "$#" -ge 2 ] || { echo "Usage: wiretap.sh SPEC COMMAND [ARGS...]" >&2; exit 2; }
spec="$1"
shift
artifacts="${VALIDATION_ARTIFACTS:-validation-artifacts}"
port="${WIRETAP_PORT:-9090}"
url="http://127.0.0.1:$port"
log="$artifacts/wiretap.log"
report="$artifacts/wiretap-report.json"
probe="/1.3/zone"                # UpCloud API constants: every SDK targets the same API.
canary="/1.3/server/not-a-uuid"  # Invalid UUID: Wiretap must reject and report it.

mkdir -p "$artifacts"
rm -f "$report"
wiretap --spec "$spec" --mock-mode --hard-validation --stream-report \
  --report-filename "$report" --port "$port" >"$log" 2>&1 &
pid=$!
trap 'kill "$pid" 2>/dev/null || true' EXIT

http_status() {
  curl -s --noproxy '*' --max-time 5 -o /dev/null -w '%{http_code}' \
    -H 'Authorization: Bearer wiretap' "$url$1" || true
}

for attempt in $(seq 120); do
  kill -0 "$pid" 2>/dev/null || { echo "ERROR: Wiretap exited; see $log" >&2; exit 1; }
  [ "$(http_status "$probe")" = 200 ] && break
  [ "$attempt" -lt 120 ] || { echo "ERROR: Wiretap not ready within 60 seconds; see $log" >&2; exit 1; }
  sleep 0.5
done

canary_status="$(http_status "$canary")"
[ "$canary_status" = 422 ] || { echo "ERROR: canary returned $canary_status, expected 422" >&2; exit 1; }

command_status=0
WIRETAP_URL="$url" "$@" || command_status=$?

if ! kill "$pid" 2>/dev/null; then
  echo "WARNING: Wiretap exited before the command finished; see $log" >&2
fi
wait "$pid" 2>/dev/null || true  # Status of a terminated or crashed Wiretap is not used.
trap - EXIT

# The report is JSONL: one violation object per line.
report_status=0
if counts="$(jq -rs --arg canary "$canary" \
  'map(.requestPath == $canary and .validationType == "parameter")
   | "\(map(select(.)) | length) \(map(select(not)) | length)"' "$report" 2>/dev/null)"; then
  read -r canaries others <<<"$counts"
  echo "Wiretap: $canaries canary violation(s), $others other violation(s). Report: $report"
  [ "$canaries" -gt 0 ] || { echo "ERROR: Wiretap did not report the canary request" >&2; report_status=1; }
  [ "$others" -eq 0 ] || { echo "ERROR: Wiretap reported contract violations; see $report" >&2; report_status=1; }
else
  echo "ERROR: missing or unreadable Wiretap report $report; see $log" >&2
  report_status=1
fi

[ "$command_status" -ne 0 ] && exit "$command_status"
exit "$report_status"
