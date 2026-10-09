#!/usr/bin/env bash
# Run live mdtest examples against the local SDK: run_examples.sh NAME...
# Each NAME maps to examples/<name>/test_<name with - as _>.md.
# Creates real UpCloud resources; requires UPCLOUD_TOKEN and mdtest.
set -euo pipefail

script="${BASH_SOURCE[0]}"
[[ "$script" == */* ]] || script="./$script"
root="$(cd "${script%/*}/../.." && pwd)"
usage="Usage: run_examples.sh NAME... (NAME is a directory under examples/)"

[ "$#" -gt 0 ] || { echo "$usage" >&2; exit 2; }
documents=()
for name in "$@"; do
  document="$root/examples/$name/test_${name//-/_}.md"
  if [[ ! "$name" =~ ^[a-z0-9-]+$ ]] || [ ! -f "$document" ]; then
    echo "ERROR: unknown example: $name" >&2
    echo "$usage" >&2
    exit 2
  fi
  documents+=("$document")
done

[ -n "${UPCLOUD_TOKEN:-}" ] || { echo "ERROR: UPCLOUD_TOKEN is required; use a separate development account" >&2; exit 1; }
command -v mdtest >/dev/null || { echo "ERROR: mdtest is required; install it before running live examples" >&2; exit 1; }

export UPCLOUD_SDK_PATH="$root"
cd "$root"
for document in "${documents[@]}"; do
  mdtest "$document"
done
