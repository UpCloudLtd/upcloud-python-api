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

The [mise](https://mise.jdx.dev/) configuration pins `uv` tooling, and its
`generate` task invokes `generator/scripts/generate.sh` under the selected Python
environment, using the checked-in `generator/openapi/spec.json` (no download).
`mise run regenerate` runs `generate`, then `lock`, then `validate` (including
Wiretap). The lock is updated before validation because validation runs with
`uv run --locked`. The first failing step stops the task with a non-zero exit,
and the generated changes and lockfile stay in place for investigation.

`generate.sh` patches the spec, then recreates only `upcloud_api/`. Do not hand-edit
`upcloud_api/` except via generator templates or `generator/scripts/patch_openapi.py`.

## Development

Install [mise](https://mise.jdx.dev/getting-started.html), then set up the locked
environment (Python 3.14 by default):

```bash
mise trust .config/mise.toml
mise install
mise run setup
mise run lint
mise run test
mise run build
```

Local development and CI use the same task entry points and pinned `uv` version.
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
| `lint` | Run all pre-commit checks. |
| `test:preprocess` | Run all generator tests: spec preprocessing, endpoint checker, downloader, example runner, and validation script. |
| `test:unit` | Run generated SDK smoke and validation-harness unit tests. |
| `check:endpoints` | Check that every spec operation has a generated method/path contract. |
| `test` | Run `test:preprocess`, `test:unit`, and `check:endpoints`, collecting failures. No Wiretap needed. |
| `test:wiretap` | Exercise generated sync/async SDK calls against a local Wiretap mock server. |
| `validate` | Run `test` checks and Wiretap, even if quick checks fail. |
| `build` | Build a wheel and source distribution into `dist/`. |
| `ci` | Run lint, `validate` (including Wiretap), and build; fail if any task fails. |
| `generate` | Regenerate the SDK from the checked-in spec. |
| `lock` | Update `uv.lock`. |
| `version:set <version>` | Explicitly change `[project].version` in `pyproject.toml` with `uv version --frozen`. |
| `spec:download <version> <asset_url>` | Download a released spec using `SPECS_ACCESS_PAT` (used by the regeneration workflow). |
| `regenerate` | Run generate, lock, and validate in order; stop at the first failure. |
| `examples:<api>` | Run one live mdtest document: `file-storage`, `object-storage`, `tag`, or `kubernetes`. |
| `examples` | Run all four live examples sequentially. |

`ci` never downloads specs, regenerates source, changes the package version, or
runs live examples. `mise install` installs the pinned `uv`, `jq`, and `wiretap`
tools. Wiretap (used by `test:wiretap`, `validate`, `ci`, and `regenerate`) runs
as a local binary in mock mode; it doesn't need Docker or Podman. No validation
task needs UpCloud credentials or makes real UpCloud requests, but the first run
needs network access to install tools and dependencies.

The existing endpoint and Wiretap findings remain strict failures, not exemptions.
`generator/scripts/wiretap.sh` starts Wiretap, sends a deliberately invalid canary
request, runs the Python tests, and then fails if the report is missing, lacks the
canary, or contains any other violation. It writes `wiretap.log` and
`wiretap-report.json`; the Python tests add the `coverage.json` case inventory.
All three go to `validation-artifacts/` (override with `VALIDATION_ARTIFACTS`). CI
uploads these diagnostics. The Regenerate workflow runs `mise run regenerate` as a plain step
before its Create PR step, so any generate, lock, or validation failure fails the
job and no PR is created.

### Task names across SDK repositories

The task names (`setup`, `lint`, `test`, `validate`, `build`, `generate`,
`regenerate`, `spec:download`, `version:set`, `examples:*`, `test:wiretap`) are the
portable interface. Go and PHP SDK repositories can use the same names.

These Bash scripts don't depend on the SDK language and can be copied unchanged
into other UpCloud SDK repositories (they need `bash`, `curl`, `tar`, and the
mise-pinned `jq` and `wiretap`):

- `generator/scripts/wiretap.sh SPEC COMMAND...` runs `COMMAND` with `WIRETAP_URL`
  pointing at a local Wiretap mock (`WIRETAP_PORT`, default 9090) and writes its
  artifacts to `VALIDATION_ARTIFACTS`. The exit code is the result.
- `generator/scripts/download_spec.sh` downloads and validates a release spec.
- `generator/scripts/run_examples.sh NAME...` runs
  `examples/<name>/test_<name with - as _>.md` with mdtest.

The rest is specific to this Python repository: `uv`, `validate.sh`,
`generate.sh`, `patch_openapi.py`, `check_endpoint_coverage.py`, the
spec-derived Wiretap cases in `tests/wiretap_cases.py`, and the SDK calls in
`tests/test_wiretap.py`.

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

The root is the distributable `upcloud-api` package. Install
[mdtest](https://github.com/UpCloudLtd/mdtest) and set `UPCLOUD_TOKEN` for a separate
development account before running a live example:

```bash
mise run examples:tag
# Explicitly run all four live resource tests:
mise run examples
```

These tasks create real UpCloud resources and can incur charges. They run
`generator/scripts/run_examples.sh`, which maps each name to
`examples/<name>/test_<name>.md` (with `-` replaced by `_` in the file name),
checks the token and mdtest availability before invocation, and sets the absolute
`UPCLOUD_SDK_PATH` so mdtest imports the local SDK from its temporary
working directory. CI retains its mdtest/Go setup action and invokes the same tasks.

After `mise run generate`, run `mise run lock` to update the lockfile, or use
`mise run regenerate` to run generate, lock, and validate in order.
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
