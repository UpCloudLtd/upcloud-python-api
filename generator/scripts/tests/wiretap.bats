#!/usr/bin/env bats
# Test wiretap.sh with fake wiretap and curl binaries (jq is real).

bats_require_minimum_version 1.5.0

CANARY='{"requestPath":"/1.3/server/not-a-uuid","validationType":"parameter"}'
OTHER='{"requestPath":"/1.3/zone","validationType":"response"}'

setup() {
  script="$BATS_TEST_DIRNAME/../wiretap.sh"
  bin="$BATS_TEST_TMPDIR/bin"
  mkdir -p "$bin"
  # Writes FAKE_REPORT (if set) as the report, marks itself ready, and serves until killed.
  cat >"$bin/wiretap" <<'EOF'
#!/bin/sh
while [ "$#" -gt 0 ]; do
  [ "$1" = --report-filename ] && report="$2"
  shift
done
[ -n "${FAKE_EXIT_EARLY:-}" ] && exit 1
[ -n "${FAKE_REPORT+set}" ] && printf '%s\n' "$FAKE_REPORT" >"$report"
touch "$FAKE_STATE/ready"
exec sleep 60 3>&-
EOF
  # Answers like Wiretap: 200 for the probe and 422 for the canary once ready.
  cat >"$bin/curl" <<'EOF'
#!/bin/sh
for url; do :; done
[ -e "$FAKE_STATE/ready" ] || { printf 000; exit 7; }
case "$url" in
  */1.3/zone) printf 200 ;;
  */1.3/server/not-a-uuid) printf '%s' "${FAKE_CANARY_STATUS:-422}" ;;
  *) printf 404 ;;
esac
EOF
  chmod +x "$bin/wiretap" "$bin/curl"
  export PATH="$bin:$PATH" FAKE_STATE="$BATS_TEST_TMPDIR" WIRETAP_PORT=19090
  export VALIDATION_ARTIFACTS="$BATS_TEST_TMPDIR/artifacts" FAKE_REPORT="$CANARY"
  unset FAKE_EXIT_EARLY FAKE_CANARY_STATUS
}

# The command records the URL it was given, then exits with $1.
contract() {
  # The child sh expands this program, not the test shell.
  # shellcheck disable=SC2016
  run --separate-stderr bash "$script" spec.json \
    sh -c 'printf %s "$WIRETAP_URL" >"$FAKE_STATE/url"; exit "$1"' sh "${1:-0}"
}

@test "passes when the command succeeds and only the canary is reported" {
  contract
  [ "$status" -eq 0 ]
  [ "$(cat "$BATS_TEST_TMPDIR/url")" = "http://127.0.0.1:19090" ]
  [[ "$output" == *"1 canary violation(s), 0 other violation(s)"* ]]
  [ -e "$VALIDATION_ARTIFACTS/wiretap.log" ]
}

@test "fails when the report lacks the canary" {
  FAKE_REPORT="" contract
  [ "$status" -eq 1 ]
  [[ "$stderr" == *"did not report the canary"* ]]
}

@test "fails when Wiretap does not reject the canary request" {
  FAKE_CANARY_STATUS=200 contract
  [ "$status" -eq 1 ]
  [[ "$stderr" == *"canary returned 200, expected 422"* ]]
  [ ! -e "$BATS_TEST_TMPDIR/url" ]
}

@test "fails on any violation besides the canary" {
  FAKE_REPORT="$CANARY"$'\n'"$OTHER" contract
  [ "$status" -eq 1 ]
  [[ "$output" == *"1 canary violation(s), 1 other violation(s)"* ]]
  [[ "$stderr" == *"reported contract violations"* ]]
}

@test "fails when the report is missing" {
  unset FAKE_REPORT
  contract
  [ "$status" -eq 1 ]
  [[ "$stderr" == *"missing or unreadable Wiretap report"* ]]
}

@test "propagates the command's failure status even with a clean report" {
  contract 3
  [ "$status" -eq 3 ]
}

@test "fails when Wiretap exits before it is ready" {
  FAKE_EXIT_EARLY=1 contract
  [ "$status" -eq 1 ]
  [[ "$stderr" == *"Wiretap exited"* ]]
  [ ! -e "$BATS_TEST_TMPDIR/url" ]
}
