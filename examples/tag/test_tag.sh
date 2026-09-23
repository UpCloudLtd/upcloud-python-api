#!/bin/bash
set -e

echo "======================================"
echo "Testing Tag API"
echo "======================================"

# Create temporary virtualenv
VENV_DIR=$(mktemp -d)
trap "rm -rf $VENV_DIR" EXIT

echo "== Create clean virtualenv =="
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

echo "== Install upcloud-api + test deps from TestPyPI =="
pip install --quiet --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ upcloud-api

echo ""
echo "== Test Tag API =="
python3 test_tag.py

echo ""
echo "== Cleanup =="
deactivate
echo "✓ Done"
