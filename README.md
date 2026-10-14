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
`mise run regenerate` runs `generate`, then `check`, and stops at the
first failure with a non-zero exit. The generated changes stay in place for
investigation. Neither task changes `pyproject.toml` or `uv.lock`. A stale lock
fails the `uv` commands, and only `mise run lock` and `mise run version:set` update it.

`generate.sh` applies `generator/openapi/overlay.yaml` with
`speakeasy overlay apply --strict`, runs the jq filter in
`generator/scripts/strip_schema_titles.jq` to remove collision-prone schema titles,
and writes the result to `generator/openapi/spec.patched.json`,
then recreates only `upcloud_api/`. Spec fixes go in the overlay. Do not hand-edit
`upcloud_api/` except via the overlay, generator templates, or
the title filter. `mise run check:generated` fails
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
| `test:tools` | Test the shell scripts offline with bats. |
| `test:preprocess` | Test schema-title filtering, overlay fixes, and the endpoint checker. |
| `test:unit` | Run offline unit tests for the SDK and Wiretap test cases. |
| `check:generated` | Regenerate and fail if `upcloud_api/` or `spec.patched.json` changes. |
| `check:endpoints` | Check that every spec operation has generated code. |
| `test:contract` | Run generated sync/async SDK calls against a local Wiretap mock. |
| `check` | Run required checks: `lint`, `test:tools`, `test:preprocess`, `test:unit`, `check:generated`. Alias: `test`. |
| `findings` | Run `check:endpoints` and `test:contract` (fails on known spec and generator issues). |
| `validate` | Run `check` and `findings`, even if `check` fails. |
| `build` | Build a wheel and source distribution into `dist/`, then run `twine check`. |
| `generate [--force]` | Regenerate the SDK from the checked-in spec. |
| `regenerate` | Run `generate`, then `check`, and stop at the first failure. |
| `lock` | Update `uv.lock`. |
| `version:set <version>` | Set `[project].version` in `pyproject.toml` and `uv.lock` with `uv version --no-sync`. |
| `spec:download <version> <asset_url>` | Download a released spec using `SPECS_ACCESS_PAT` (used by the regeneration workflow). |
| `examples [name...]` | Run live mdtest examples, all four by default. |

### Checks and contract tests

`check` runs the required static, unit, and generation checks. It blocks builds,
releases, and regeneration PRs.

`findings` runs `check:endpoints` and `test:contract` to report known spec and
generator issues without blocking releases. Regeneration PRs are opened as
drafts when `findings` fails.

`mise install` installs every pinned tool, including `wiretap`, `bats`,
`shellcheck`, `actionlint`, `twine`, and `mdtest` (built with the pinned Go).
Wiretap runs as a local binary in mock mode and doesn't need Docker or Podman.
No task except `examples` needs UpCloud credentials or makes real UpCloud requests,
but the first run needs network access to install tools and dependencies.

`generator/scripts/wiretap.sh` starts Wiretap, sends an invalid probe request to
verify validation is active, runs the Python tests, and fails if the report is
missing or contains any other violation. It writes `wiretap.log`,
`wiretap-report.json`, and `coverage.json` to `validation-artifacts/` (override
with `VALIDATION_ARTIFACTS`).

### Shared scripts across SDK repositories

The task names are shared across the Python, Go, and PHP SDK repositories:
`setup`, `lint`, `generate`, `test:tools`, `test:preprocess`, `test:unit`,
`check:generated`, `check:endpoints`, `test:contract`, `check`, `findings`,
`build`, `spec:download`, `regenerate`, `examples`, and `version:set`. Only the
`run` commands are language-specific.

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
`generator/openapi/overlay.yaml`, `strip_schema_titles.jq`, `check_endpoint_coverage.py`,
the spec-derived Wiretap cases
in `tests/wiretap_cases.py`, and the SDK calls in `tests/test_wiretap.py`.

Local generation always uses the checked-in `generator/openapi/spec.json`.
`spec:download` is only needed by the CI regeneration workflow, or when you
deliberately want a newer released spec.

### Downloading a spec and preparing a package version

Downloading is optional. Set `SPECS_ACCESS_PAT` in your shell before downloading a
release asset. The URL
must be a GitHub API release-asset URL. `--spec-file` selects the tarball member and
defaults to `upcloud-public-openapi.json`:

```bash
mise run spec:download 0.0.107 \
  https://api.github.com/repos/UpCloudLtd/upcloud-openapi-spec/releases/assets/123 \
  --spec-file upcloud-public-openapi.json
mise run regenerate
```

Downloading replaces `generator/openapi/spec.json` only after the selected member
has been downloaded and checked as an OpenAPI JSON document. The token is sent only
to `api.github.com`. curl doesn't forward it when the asset redirects to another
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
separate development account before running a live example. `mise install`
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
dispatches. Fork PRs are skipped because they cannot read the token.

`SPEC_VERSION` follows the OpenAPI spec, while the package version is tracked in the root
`pyproject.toml` and `uv.lock`. The v3 release
workflows update it from the release tag or manual TestPyPI input (for example,
`3.0.0a1`) via `mise run version:set` before building.
The root `pyproject.toml`, README, and license are not overwritten by regeneration.

## Changelog

- Changelog is available [in its own file](CHANGELOG.md)

## Bugs, Issues, Problems, Ideas

Please report issues and feature requests through
[the issues page](https://github.com/UpCloudLtd/upcloud-python-api/issues).
