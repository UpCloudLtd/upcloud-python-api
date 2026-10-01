#!/usr/bin/env bash
set -euo pipefail

mode="${1:-all}"
status=0

case "$mode" in
  quick|all)
    python -m unittest discover -s generator/tests -p 'test_*.py' || status=1
    python -m unittest tests.test_sdk_smoke tests.test_wiretap_cases tests.test_wiretap_lifecycle || status=1
    python generator/tests/check_endpoint_coverage.py \
      generator/openapi/spec.json generator/openapi/spec.patched.json upcloud_api/api || status=1
    ;;
  wiretap) ;;
  *) echo "Usage: validate.sh [quick|wiretap|all]" >&2; exit 2 ;;
esac

if [ "$mode" = wiretap ] || [ "$mode" = all ]; then
  export VALIDATION_ARTIFACTS="${VALIDATION_ARTIFACTS:-validation-artifacts}"
  python -m unittest tests.test_wiretap || status=1
fi

exit "$status"
