#!/usr/bin/env bash
# Download an OpenAPI spec from a GitHub release asset (a tarball) and replace
# the output only after it validates. Requires SPECS_ACCESS_PAT, curl, tar, jq.
# The token goes only to api.github.com; curl drops it on cross-host redirects.
# Copied unchanged into each UpCloud SDK repository; jq comes from mise.
set -euo pipefail

usage="Usage: download_spec.sh --version V --asset-url URL [--spec-file NAME] [--output PATH]"
die() { echo "ERROR: $*" >&2; exit 1; }

spec_file="upcloud-public-openapi.json"
output="generator/openapi/spec.json"
while [ "$#" -gt 0 ]; do
  [ "$#" -ge 2 ] || { echo "$usage" >&2; exit 2; }
  case "$1" in
    --version) version="$2" ;;
    --asset-url) asset_url="$2" ;;
    --spec-file) spec_file="$2" ;;
    --output) output="$2" ;;
    *) echo "$usage" >&2; exit 2 ;;
  esac
  shift 2
done
[ -n "${version+set}" ] && [ -n "${asset_url+set}" ] || { echo "$usage" >&2; exit 2; }

[[ "$version" =~ [^[:space:]] ]] || die "spec version is required"
[[ "$asset_url" =~ ^https://api\.github\.com/repos/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/releases/assets/[0-9]+$ ]] ||
  die "asset URL must be an HTTPS api.github.com release asset endpoint"
[ -n "${SPECS_ACCESS_PAT:-}" ] || die "SPECS_ACCESS_PAT is required"
[ -n "$spec_file" ] || die "spec file name is required"

echo "Downloading OpenAPI specification for version $version"
mkdir -p "$(dirname "$output")"
tmp="$(mktemp -d "$(dirname "$output")/.download-spec.XXXXXX")"
trap 'rm -rf "$tmp"' EXIT

# printf is a builtin, so the token never appears in any process's arguments.
printf 'Authorization: Bearer %s\n' "$SPECS_ACCESS_PAT" |
  curl -fsSL --proto =https --proto-redir =https --retry 5 --connect-timeout 30 --max-time 300 \
    -H 'Accept: application/octet-stream' -H @- -o "$tmp/asset" "$asset_url" ||
  die "release asset download failed"

# Read only the requested member to stdout; nothing is written by archive path.
tar -xOf "$tmp/asset" -- "$spec_file" >"$tmp/spec.json" || die "archive has no member $spec_file"

jq -es 'length == 1 and (.[0] | (.openapi | type == "string" and length > 0)
  and (.info | type == "object") and (.paths | type == "object"))' "$tmp/spec.json" >/dev/null 2>&1 ||
  die "$spec_file is not a valid OpenAPI document"

mv -f "$tmp/spec.json" "$output"
