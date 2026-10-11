# UpCloud's Python API Client (v3 alpha)

[![test](https://github.com/UpCloudLtd/upcloud-python-api/actions/workflows/main.yml/badge.svg)](https://github.com/UpCloudLtd/upcloud-python-api/actions/workflows/main.yml)
[![PyPI version](https://badge.fury.io/py/upcloud-api.svg)](https://badge.fury.io/py/upcloud-api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/UpCloudLtd/upcloud-python-api/blob/main/LICENSE.txt)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/UpCloudLtd/upcloud-python-api/badge)](https://scorecard.dev/viewer/?uri=github.com%2FUpCloudLtd%2Fupcloud-python-api)

This **`v3-dev`** branch is the generated OpenAPI client for UpCloud's HTTP API (`/1.3/...`). It is a **breaking** major relative to the handwritten 2.x `CloudManager` client on `main`. “v3” is the Python package major version, not a new HTTP API version.

Please test thoroughly before production use. A separate UpCloud account for development is recommended.

## Installation

Stable 2.x remains the default on PyPI. Once a v3 alpha is published, select it explicitly:

```bash
pip install upcloud-api               # latest 2.x (currently 2.9.x)
pip install "upcloud-api==3.0.0a1"    # this generated v3 alpha
```

Do **not** rely on a blanket `pip install --pre`. That would also pull pre-releases of other dependencies.

`upcloud-api>=2.9,<3` stays on 2.x: under PEP 440, `<3` excludes `3.0.0a1` even with `--pre`. To opt into the v3 alpha, pin `upcloud-api==3.0.0a1`.

The distribution name is `upcloud-api`. The import package is `upcloud_api`.

### Supported Python versions

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14
- PyPy 3.11

## Usage

```python
import os
from upcloud_api import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.upcloud.com",
    token=os.environ["UPCLOUD_TOKEN"],
)

# Call generated operations, for example:
# from upcloud_api.api.server import list_servers
# with client as client:
#     servers = list_servers.sync(client=client)
```

This is not a drop-in replacement for `CloudManager`. See generated helpers under `upcloud_api/` and examples under `examples/`.

## Regenerating the client

The client is produced by `openapi-python-client` from the public OpenAPI spec:

```bash
mise trust .config/mise.toml
mise install
mise run generate
```

The [mise](https://mise.jdx.dev/) configuration pins `openapi-python-client`,
`speakeasy`, the `ruff` its post-hooks use (the same version as the pre-commit hook),
`jq`, and `uv`.
The `generate` task runs `generator/scripts/generate.sh` on the checked-in
`generator/openapi/spec.json` (no download). It refuses to overwrite uncommitted
changes in `upcloud_api/` unless you pass `mise run generate --force`.
`mise run regenerate` runs `generate`, then the `check` gate, and stops at the
first failure with a non-zero exit; the generated changes stay in place for
investigation. Neither task changes `pyproject.toml` or `uv.lock`; a stale lock
fails the `uv` commands, and only `mise run lock` updates it.

`generate.sh` applies `generator/openapi/overlay.yaml` with
`speakeasy overlay apply --strict`, runs `generator/scripts/patch_openapi.py` to
remove schema titles only, writes the result to `generator/openapi/spec.patched.json`,
then recreates only `upcloud_api/`. Spec fixes go in the overlay. Do not hand-edit
`upcloud_api/` except via the overlay, generator templates, or
`generator/scripts/patch_openapi.py`. `mise run check:generated` fails
if regenerating changes either output.

## Development

Install [mise](https://mise.jdx.dev/getting-started.html), then set up the locked
environment (Python 3.14 by default):

```bash
mise trust .config/mise.toml
mise install
mise run setup
mise run lint
mise run check
mise run build
```

Local development and CI use the same task entry points and mise-pinned tools.
Every `uv` command runs with `UV_LOCKED=1`, so it fails on a stale `uv.lock`.
Python is selected by `UV_PYTHON`, or `.python-version` when no override is supplied.
For example:

```bash
UV_PYTHON=3.11 mise run test:unit
UV_PYTHON=pypy3.11 mise run test:unit
```

### Task reference

| Task | Purpose |
| --- | --- |
| `setup` | Install locked development dependencies. |
| `lint` | Run pre-commit: ruff, shellcheck, and actionlint. |
| `test:tools` | L1: test the shared shell scripts offline with bats. |
| `test:preprocess` | L2: test spec patching (`test_patch_openapi.py`, `test_openapi_overlay.py`) and the endpoint checker. |
| `test:unit` | L4: test the generated SDK and the contract-case derivation offline. |
| `check:generated` | L3: regenerate and fail if `upcloud_api/` or `spec.patched.json` changes. |
| `check:endpoints` | L3: check that every spec operation has a generated method/path contract. |
| `test:contract` | L5: run generated sync/async SDK calls against a local Wiretap mock. |
| `check` | Integrity gate: `lint`, `test:tools`, `test:preprocess`, `test:unit`, `check:generated`. Must be green. Alias: `test`. |
| `findings` | Findings gate: `check:endpoints` and `test:contract`, run even if one fails. Red on known defects. |
| `validate` | Run `check` and `findings`, even if `check` fails. Kept for one release. |
| `build` | Build a wheel and source distribution into `dist/`, then run `twine check`. |
| `generate [--force]` | Regenerate the SDK from the checked-in spec. |
| `regenerate` | Run `generate`, then `check`; stop at the first failure. |
| `lock` | Update `uv.lock` (the only task that may change it). |
| `version:set <version>` | Explicitly change `[project].version` in `pyproject.toml` with `uv version --frozen`. |
| `spec:download <version> <asset_url>` | Download a released spec using `SPECS_ACCESS_PAT` (used by the regeneration workflow). |
| `examples [name...]` | L6: run live mdtest documents, all four by default. |

### Test layers and gates

Every check belongs to one layer, and every defect fails exactly one check.

| Layer | Guards | Members |
| --- | --- | --- |
| L1 tools | The shared shell scripts behave safely. | `generator/scripts/tests/*.bats` |
| L2 preprocess | Spec patches are correct and idempotent. | `generator/tests/test_patch_openapi.py`, `test_openapi_overlay.py`, `test_endpoint_coverage.py` |
| L3 generation | Committed output equals generator output; every spec operation is generated. | `check:generated`, `check:endpoints` |
| L4 SDK unit | Generated imports, enums, `client.py.jinja` behavior, contract-case derivation. | `tests/test_sdk_smoke.py`, `tests/test_wiretap_cases.py` |
| L5 contract | SDK calls match the spec on the wire. | `tests/test_wiretap.py` via `wiretap.sh` |
| L6 live | Real API behavior. | `examples/**/*.md` via mdtest |

There are two gates. `check` (integrity) must always be green: a red `check`
means the pipeline itself is broken. It blocks builds, releases, and regeneration
PRs. `findings` covers the known spec and generator defects: a red `findings`
means the spec or generator still has a known defect. It always runs and uploads
its diagnostics, but it does not block releases. Regeneration PRs are opened as
drafts while it fails.

`mise install` installs every pinned tool, including `wiretap`, `bats`,
`shellcheck`, `actionlint`, `twine`, and `mdtest` (built with the pinned Go).
Wiretap runs as a local binary in mock mode; it doesn't need Docker or Podman.
No task except `examples` needs UpCloud credentials or makes real UpCloud requests,
but the first run needs network access to install tools and dependencies.

The existing endpoint and Wiretap findings remain strict failures, not exemptions.
`generator/scripts/wiretap.sh` starts Wiretap, sends a deliberately invalid canary
request, runs the Python tests, and then fails if the report is missing, lacks the
canary, or contains any other violation. It writes `wiretap.log` and
`wiretap-report.json`; the Python tests add the `coverage.json` case inventory,
which lists operations without generated code under `missing` (`check:endpoints`
reports them as failures). All three go to `validation-artifacts/` (override with
`VALIDATION_ARTIFACTS`). CI uploads these diagnostics.

### Task names across SDK repositories

The task names, their inputs, and their exit semantics are the portable interface:
`setup`, `lint`, `generate`, `test:tools`, `test:preprocess`, `test:unit`,
`check:generated`, `check:endpoints`, `test:contract`, `check`, `findings`,
`build`, `spec:download`, `regenerate`, `examples`, and `version:set`. Go and PHP
SDK repositories can use the same names; only the `run` bodies are
language-specific.

Scripts with the header line `Copied unchanged into each UpCloud SDK repository`
don't depend on the SDK language. They need only `bash`, `git`, `curl`, `tar`, and
mise-pinned tools, and their bats tests in `generator/scripts/tests/` travel with
them:

- `generator/scripts/wiretap.sh SPEC COMMAND...` runs `COMMAND` with `WIRETAP_URL`
  pointing at a local Wiretap mock (`WIRETAP_PORT`, default 9090) and writes its
  artifacts to `VALIDATION_ARTIFACTS`. The exit code is the result.
- `generator/scripts/check_generated.sh PATH... -- CMD...` runs `CMD` and fails,
  listing the files, if it changed any `PATH`.
- `generator/scripts/download_spec.sh` downloads and validates a release spec.
- `generator/scripts/run_examples.sh NAME...` runs
  `examples/<name>/test_<name with - as _>.md` with mdtest.

The rest is specific to this Python repository: `uv`, `generate.sh`,
`generator/openapi/overlay.yaml`, `patch_openapi.py`, `check_endpoint_coverage.py`,
the spec-derived Wiretap cases
in `tests/wiretap_cases.py`, and the SDK calls in `tests/test_wiretap.py`.

Local generation always uses the checked-in `generator/openapi/spec.json`.
`spec:download` is only needed by the CI regeneration workflow, or when you
deliberately want a newer released spec.

### Downloading a spec and preparing a package version

Downloading is optional. Set `SPECS_ACCESS_PAT` in your shell before downloading a
release asset. The URL
must be a GitHub API release-asset URL; `--spec-file` selects the tarball member and
defaults to `upcloud-public-openapi.json`:

```bash
mise run spec:download 0.0.107 \
  https://api.github.com/repos/UpCloudLtd/upcloud-openapi-spec/releases/assets/123 \
  --spec-file upcloud-public-openapi.json
mise run regenerate
```

Downloading replaces `generator/openapi/spec.json` only after the selected member
has been downloaded and checked as an OpenAPI JSON document. The token is sent only
to `api.github.com`; curl doesn't forward it when the asset redirects to another
host. Use an actual release asset
ID rather than the placeholder above. Package version changes are separate and explicit:

```bash
mise run version:set 3.0.0a1
mise run build
```

Publishing, GitHub releases, PR creation, artifact handling, CodeQL, and Scorecard
remain GitHub Actions responsibilities, not local tasks.

### Live examples

The root is the distributable `upcloud-api` package. Set `UPCLOUD_TOKEN` for a
separate development account before running a live example; `mise install`
provides [mdtest](https://github.com/UpCloudLtd/mdtest):

```bash
mise run examples tag
# Explicitly run all four live resource tests:
mise run examples
```

These tasks create real UpCloud resources and can incur charges. They run
`generator/scripts/run_examples.sh`, which maps each name to
`examples/<name>/test_<name>.md` (with `-` replaced by `_` in the file name),
checks the token and mdtest availability before invocation, and sets the absolute
`UPCLOUD_SDK_PATH` so mdtest imports the local SDK from its temporary
working directory. CI runs `mise run examples` for same-repository PRs and manual
dispatches; fork PRs are skipped because they cannot read the token.

`SPEC_VERSION` follows the OpenAPI spec, while the package version in the root
`pyproject.toml` defaults to `3.0.0.dev0` for development builds. The v3 release
workflows replace it with the release tag or manual TestPyPI input (for example,
`3.0.0a1`) before building.
The root `pyproject.toml`, README, and license are not overwritten by regeneration.

## Changelog

- Changelog is available [in its own file](CHANGELOG.md)

## Bugs, Issues, Problems, Ideas

Please report issues and feature requests through
[the issues page](https://github.com/UpCloudLtd/upcloud-python-api/issues).
