#!/usr/bin/env bats
# download_spec.sh, offline: a fake curl serves a local tarball; tar and jq are real.

bats_require_minimum_version 1.5.0

URL="https://api.github.com/repos/UpCloudLtd/spec/releases/assets/123"
TOKEN="private-test-token"

setup() {
  script="$BATS_TEST_DIRNAME/../download_spec.sh"
  bin="$BATS_TEST_TMPDIR/bin"
  stage="$BATS_TEST_TMPDIR/stage"
  spec_out="$BATS_TEST_TMPDIR/out/spec.json"
  mkdir -p "$bin" "$stage" "${spec_out%/*}"
  printf original >"$spec_out"
  printf '{\n "openapi": "3.1.0", "info": {"version": "different"}, "paths": {}\n}\n' >"$BATS_TEST_TMPDIR/spec.json"
  cat >"$bin/curl" <<'EOF'
#!/bin/sh
printf '%s\n' "$@" >"$CURL_ARGS"
cat >"$CURL_STDIN"
while [ "$#" -gt 0 ]; do
  [ "$1" = -o ] && out="$2"
  shift
done
if [ "$CURL_EXIT" != 0 ]; then
  echo "curl: (22) The requested URL returned error: 404" >&2
  exit "$CURL_EXIT"
fi
cp "$FIXTURE" "$out"
EOF
  chmod +x "$bin/curl"
  export PATH="$bin:$PATH" CURL_ARGS="$BATS_TEST_TMPDIR/curl-args"
  export CURL_STDIN="$BATS_TEST_TMPDIR/curl-stdin" CURL_EXIT=0
  export FIXTURE="$BATS_TEST_TMPDIR/fixture.tar.gz" SPECS_ACCESS_PAT="$TOKEN"
}

# Archive the named files from $stage as the release asset.
archive() {
  tar -czf "$FIXTURE" -C "$stage" "$@"
}

download() {
  run --separate-stderr bash "$script" --version release-label --asset-url "$URL" \
    --output "$spec_out" "$@"
}

assert_failed_unchanged() {
  [ "$status" -ne 0 ]
  [[ "$stderr" == *ERROR:* ]]
  [ "$(cat "$spec_out")" = original ]
  [ "$(ls -A "${spec_out%/*}")" = spec.json ]
}

@test "success keeps the spec bytes and the token out of arguments and logs" {
  cp "$BATS_TEST_TMPDIR/spec.json" "$stage/upcloud-public-openapi.json"
  echo ignored >"$stage/unrelated.json"
  archive unrelated.json upcloud-public-openapi.json
  download
  [ "$status" -eq 0 ]
  cmp "$spec_out" "$BATS_TEST_TMPDIR/spec.json"
  [ "$(ls -A "${spec_out%/*}")" = spec.json ]
  [[ "$output" == *"version release-label"* ]]
  [[ "$output$stderr" != *"$TOKEN"* ]]
  grep -qF "$TOKEN" "$CURL_STDIN"
  run ! grep -qF "$TOKEN" "$CURL_ARGS"
  run ! grep -qx -- --location-trusted "$CURL_ARGS"
  [ "$(grep -x -A1 -- --proto-redir "$CURL_ARGS" | tail -1)" = "=https" ]
  [ "$(tail -1 "$CURL_ARGS")" = "$URL" ]
}

@test "bad input fails before curl runs" {
  for url in "${URL/https:/http:}" "${URL/api.github.com/example.com}" "$URL/x"; do
    URL="$url" download
    [ "$status" -eq 1 ]
    [[ "$stderr" == ERROR:* ]]
  done
  SPECS_ACCESS_PAT="" download
  [ "$status" -eq 1 ]
  [[ "$stderr" == ERROR:* ]]
  download --bogus x
  [ "$status" -eq 2 ]
  [ ! -e "$CURL_ARGS" ]
  [ "$(cat "$spec_out")" = original ]
}

@test "bad archive content leaves the output unchanged" {
  cp "$BATS_TEST_TMPDIR/spec.json" "$stage/other.json"
  archive other.json
  download
  assert_failed_unchanged

  printf '{"openapi": "3.1.0", "paths": {}}' >"$stage/upcloud-public-openapi.json"
  archive upcloud-public-openapi.json
  download
  assert_failed_unchanged

  printf '{' >"$stage/upcloud-public-openapi.json"
  archive upcloud-public-openapi.json
  download
  assert_failed_unchanged

  ln -sf ../outside "$stage/upcloud-public-openapi.json"
  archive upcloud-public-openapi.json
  download
  assert_failed_unchanged
}

@test "curl failure leaves the output unchanged without leaking the token" {
  archive .
  CURL_EXIT=22 download
  assert_failed_unchanged
  [[ "$output$stderr" != *"$TOKEN"* ]]
}
