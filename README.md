# UpCloud's Python API Client (v3 alpha)

[![test](https://github.com/UpCloudLtd/upcloud-python-api/actions/workflows/main.yml/badge.svg)](https://github.com/UpCloudLtd/upcloud-python-api/actions/workflows/main.yml)
[![PyPI version](https://badge.fury.io/py/upcloud-api.svg)](https://badge.fury.io/py/upcloud-api)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/UpCloudLtd/upcloud-python-api/blob/main/LICENSE.txt)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/UpCloudLtd/upcloud-python-api/badge)](https://scorecard.dev/viewer/?uri=github.com%2FUpCloudLtd%2Fupcloud-python-api)

This **`v3-dev`** branch is the generated OpenAPI client for UpCloud's HTTP API (`/1.3/...`). It is a **breaking** major relative to the handwritten 2.x `CloudManager` client on `main`. “v3” is the Python package major version, not a new HTTP API version.

Please test thoroughly before production use. A separate UpCloud account for development is recommended.

## Installation

Stable 2.x remains the default on PyPI:

```bash
pip install upcloud-api               # latest 2.x (currently 2.9.x)
pip install "upcloud-api==3.0.0a1"    # this generated v3 alpha
```

Do **not** rely on a blanket `pip install --pre`. That would also pull pre-releases of other dependencies.

**Ansible / version specifiers:** `upcloud-api>=2.9,<3` still matches `3.0.0a1` because `3.0.0a1 < 3.0.0`. Without `--pre`, pip stays on 2.x. To stay on 2.x even with `--pre`, pin `upcloud-api~=2.9.0` or `upcloud-api>=2.9.0,<3.0.0.dev0`. To opt into v3 alpha, pin `upcloud-api==3.0.0a1`.

The distribution name is `upcloud-api`. The import package is `upcloud_api`.

### Supported Python versions

- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

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

This is not a drop-in replacement for `CloudManager`. See generated helpers under `sdk/README.md` and examples under `examples/`.

## Regenerating the client

The client is produced by `openapi-python-client` from the public OpenAPI spec:

```bash
cp /path/to/upcloud-public-openapi.json generator/openapi/spec.json
generator/scripts/generate.sh
```

`generate.sh` patches the spec, then recreates `sdk/`. Do not hand-edit `sdk/upcloud_api/` except via generator templates or `generator/scripts/patch_openapi.py`.

## Changelog

- Changelog is available [in its own file](CHANGELOG.md)

## Bugs, Issues, Problems, Ideas

Please report issues and feature requests through
[the issues page](https://github.com/UpCloudLtd/upcloud-python-api/issues).
