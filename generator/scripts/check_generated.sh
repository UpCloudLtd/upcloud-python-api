#!/usr/bin/env bash
# Fail if CMD changes any PATH: check_generated.sh PATH... -- CMD [ARGS...]
# PATHs are compared with their state before CMD ran, so on a clean tree this
# proves the committed output equals the generator output. Prints changed files.
# PATHs are restored to their exact pre-CMD state afterwards, even if CMD fails.
# Copied unchanged into each UpCloud SDK repository; uses only bash, git, and tar.
set -euo pipefail

usage="Usage: check_generated.sh PATH... -- CMD [ARGS...]"
paths=()
while [ "$#" -gt 0 ] && [ "$1" != -- ]; do
  paths+=("$1")
  shift
done
[ "${#paths[@]}" -gt 0 ] && [ "$#" -ge 2 ] || { echo "$usage" >&2; exit 2; }
shift
# PATHs are deleted and restored, so only plain relative paths are accepted.
for path in "${paths[@]}"; do
  case "/$path/" in
    //* | */./* | */../* | /-*)
      echo "$usage (PATH must be relative, without . or .. components: $path)" >&2
      exit 2
      ;;
  esac
done

# Snapshot PATHs into a private index; the real index and CMD's git are untouched.
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
snapshot() { GIT_INDEX_FILE="$tmp/index" git "$@"; }
snapshot read-tree HEAD
snapshot add -A -- "${paths[@]}"

# Back up PATHs byte-for-byte (ignored files included) to restore after CMD.
existing=()
for path in "${paths[@]}"; do
  if [ -e "$path" ] || [ -L "$path" ]; then existing+=("$path"); fi
done
if [ "${#existing[@]}" -gt 0 ]; then
  tar -cf "$tmp/paths.tar" -- "${existing[@]}"
fi
restore() {
  rm -rf -- "${paths[@]}" && { [ ! -f "$tmp/paths.tar" ] || tar -xpf "$tmp/paths.tar"; }
}
on_exit() {
  if restore; then
    rm -rf "$tmp"
  else
    echo "ERROR: could not restore ${paths[*]}; the backup is kept in $tmp/paths.tar" >&2
    exit 1
  fi
}
trap on_exit EXIT

cmd_status=0
"$@" || cmd_status=$?
if [ "$cmd_status" -ne 0 ]; then
  echo "ERROR: CMD failed with exit status $cmd_status" >&2
  exit "$cmd_status"
fi

status=0
snapshot --no-pager diff --exit-code --stat -- "${paths[@]}" >&2 || status=1
untracked="$(snapshot ls-files --others --exclude-standard -- "${paths[@]}")"
if [ -n "$untracked" ]; then
  echo "New files:" >&2
  echo "$untracked" >&2
  status=1
fi
if [ "$status" -ne 0 ]; then
  echo "ERROR: CMD changed the files above; regenerate and commit them" >&2
  exit 1
fi
echo "Generated output is unchanged: ${paths[*]}"
