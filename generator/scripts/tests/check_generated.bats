#!/usr/bin/env bats
# check_generated.sh in a throwaway git repository; never touches this repository.

bats_require_minimum_version 1.5.0

setup() {
  script="$BATS_TEST_DIRNAME/../check_generated.sh"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY
  export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
  repo="$BATS_TEST_TMPDIR/repo"
  mkdir -p "$repo/gen"
  cd "$repo"
  git init -q
  printf '*.cache\n' >.gitignore
  printf a >gen/a.txt
  printf b >gen/b.txt
  printf other >other.txt
  git add -A
  git -c user.name=test -c user.email=test@example.invalid commit -qm fixture
}

# Every index entry, status line (ignored included), and file content under gen/.
state() {
  git ls-files -s
  git status --porcelain --ignored --untracked-files=all
  find gen -type f | LC_ALL=C sort | while read -r file; do
    printf '%s=%s\n' "$file" "$(cat "$file")"
  done
}

check() {
  run --separate-stderr bash "$script" "$@"
}

@test "unchanged output passes" {
  before="$(state)"
  check gen -- sh -c 'rm -rf gen && mkdir gen && printf a >gen/a.txt && printf b >gen/b.txt'
  [ "$status" -eq 0 ]
  [[ "$output" == *"Generated output is unchanged: gen"* ]]
  [ "$(state)" = "$before" ]
}

@test "changed tracked files fail, are named, and are restored with local edits" {
  printf 'local edit' >gen/a.txt
  printf ignored >gen/local.cache
  before="$(state)"
  check gen -- sh -c 'rm -rf gen && mkdir gen && printf a >gen/a.txt && printf changed >gen/b.txt'
  [ "$status" -eq 1 ]
  [[ "$stderr" == *gen/a.txt* ]]
  [[ "$stderr" == *gen/b.txt* ]]
  [ "$(state)" = "$before" ]
  [ "$(cat gen/a.txt)" = "local edit" ]
  [ "$(cat gen/local.cache)" = ignored ]
}

@test "new untracked files fail, are named, and are removed; existing ones are kept" {
  printf keep >gen/keep.txt
  before="$(state)"
  check gen -- sh -c 'printf new >gen/new.txt'
  [ "$status" -eq 1 ]
  [[ "$stderr" == *"New files:"*gen/new.txt* ]]
  [[ "$stderr" != *gen/keep.txt* ]]
  [ ! -e gen/new.txt ]
  [ "$(state)" = "$before" ]
}

@test "command failure is propagated and the paths are restored" {
  before="$(state)"
  check gen -- sh -c 'printf partial >gen/a.txt; printf new >gen/new.txt; exit 3'
  [ "$status" -eq 3 ]
  [[ "$stderr" == *"CMD failed with exit status 3"* ]]
  [ "$(state)" = "$before" ]
}

@test "the real index is preserved" {
  printf staged >gen/b.txt
  git add gen/b.txt
  printf unstaged >gen/a.txt
  index="$(git ls-files -s)"
  cached="$(git diff --cached)"
  before="$(state)"
  check gen -- sh -c 'printf a >gen/a.txt && printf b >gen/b.txt'
  [ "$status" -eq 1 ]
  [ "$(git ls-files -s)" = "$index" ]
  [ "$(git diff --cached)" = "$cached" ]
  [ "$(state)" = "$before" ]
}

@test "usage errors exit 2 before the command runs" {
  for args in "" "gen" "gen --" "-- touch ran" "../gen -- touch ran" "/tmp -- touch ran" \
    ". -- touch ran" "gen/./a.txt -- touch ran" "-gen -- touch ran"; do
    # shellcheck disable=SC2086
    check $args
    [ "$status" -eq 2 ]
    [[ "$stderr" == *Usage:* ]]
  done
  [ ! -e ran ]
}
