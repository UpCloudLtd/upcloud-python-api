#!/usr/bin/env bash
set -euo pipefail

mode="${1:-all}"
status=0

preprocess() {
  python -m unittest discover -s generator/tests -p 'test_*.py'
}

unit() {
  python -m unittest tests.test_sdk_smoke tests.test_wiretap_cases
}

endpoints() {
  python generator/tests/check_endpoint_coverage.py \
    generator/openapi/spec.json generator/openapi/spec.patched.json upcloud_api/api
}

wiretap() {
  export VALIDATION_ARTIFACTS="${VALIDATION_ARTIFACTS:-validation-artifacts}"
  bash "${WIRETAP_SH:-generator/scripts/wiretap.sh}" generator/openapi/spec.patched.json \
    python -m unittest tests.test_wiretap
}

case "$mode" in
  preprocess|unit|endpoints|wiretap) "$mode" || status=1 ;;
  quick|all)
    preprocess || status=1
    unit || status=1
    endpoints || status=1
    if [ "$mode" = all ]; then
      wiretap || status=1
    fi
    ;;
  *) echo "Usage: validate.sh [preprocess|unit|endpoints|quick|wiretap|all]" >&2; exit 2 ;;
esac

exit "$status"
