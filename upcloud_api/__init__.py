"""A client library for accessing UpCloud API"""

from .client import AuthenticatedClient, Client
from .spec_version import SPEC_VERSION

__all__ = (
    "AuthenticatedClient",
    "Client",
    "SPEC_VERSION",
)
