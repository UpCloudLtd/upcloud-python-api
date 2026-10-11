#!/usr/bin/env bats
# run_examples.sh with a fake mdtest; never calls UpCloud.

bats_require_minimum_version 1.5.0

setup() {
  script="$BATS_TEST_DIRNAME/../run_examples.sh"
  root="$(cd "$BATS_TEST_DIRNAME/../../.." && pwd)"
  bin="$BATS_TEST_TMPDIR/bin"
  calls="$BATS_TEST_TMPDIR/calls"
  mkdir -p "$bin"
  cat >"$bin/mdtest" <<'EOF'
#!/bin/sh
printf '%s|%s|%s|%s\n' "$1" "$PWD" "$UPCLOUD_SDK_PATH" "$UPCLOUD_TOKEN" >>"$CALL_LOG"
case "$1" in *"$FAIL_MATCH"*) [ -n "$FAIL_MATCH" ] && exit 1 ;; esac
exit 0
EOF
  chmod +x "$bin/mdtest"
  unset TOKEN
}

# Run with only the fake mdtest on PATH, from an unrelated directory.
examples() {
  cd "$BATS_TEST_TMPDIR" || return
  run --separate-stderr env -i PATH="$bin" CALL_LOG="$calls" FAIL_MATCH="${FAIL_MATCH:-}" \
    UPCLOUD_SDK_PATH=/wrong ${TOKEN+UPCLOUD_TOKEN="$TOKEN"} "$BASH" "$script" "$@"
}

@test "missing token fails before mdtest runs" {
  examples tag
  [ "$status" -eq 1 ]
  [[ "$stderr" == *UPCLOUD_TOKEN* ]]
  [ ! -e "$calls" ]
}

@test "missing mdtest fails" {
  rm "$bin/mdtest"
  TOKEN=test-token examples tag
  [ "$status" -eq 1 ]
  [[ "$stderr" == *mdtest* ]]
}

@test "names run in order with the local SDK and stop at the first failure" {
  names=(file-storage object-storage tag kubernetes)
  expected=()
  for name in "${names[@]}"; do
    expected+=("$root/examples/$name/test_${name//-/_}.md|$root|$root|test-token")
  done
  TOKEN=test-token examples "${names[@]}"
  [ "$status" -eq 0 ]
  [ "$(cat "$calls")" = "$(printf '%s\n' "${expected[@]}")" ]
  [[ "$output$stderr" != *test-token* ]]

  rm "$calls"
  TOKEN=test-token FAIL_MATCH=test_object_storage examples "${names[@]}"
  [ "$status" -ne 0 ]
  [ "$(cat "$calls")" = "$(printf '%s\n' "${expected[@]:0:2}")" ]
}

@test "unknown or unsafe names are rejected before mdtest runs" {
  for name in unknown ../x; do
    TOKEN=test-token examples "$name"
    [ "$status" -eq 2 ]
    [[ "$stderr" == *Usage:* ]]
  done
  [ ! -e "$calls" ]
}
