import base64
import os

try:
    import keyring
except ImportError:
    keyring = None

from upcloud_api.errors import UpCloudClientError

ENV_KEY_USERNAME = "UPCLOUD_USERNAME"
ENV_KEY_PASSWORD = "UPCLOUD_PASSWORD"  # noqa: S105
ENV_KEY_TOKEN = "UPCLOUD_TOKEN"  # noqa: S105

KEYRING_SERVICE_NAME = "UpCloud"
KEYRING_TOKEN_USER = ""
KEYRING_GO_PREFIX = "go-keyring-base64:"


def _parse_keyring_value(value: str) -> str:
    if value.startswith(KEYRING_GO_PREFIX):
        value = value[len(KEYRING_GO_PREFIX) :]
        return base64.b64decode(value).decode()

    return value


def _read_keyring_value(username: str) -> str:
    if keyring is None:
        return None

    value = keyring.get_password(KEYRING_SERVICE_NAME, username)
    try:
        return _parse_keyring_value(value) if value else None
    except Exception:
        raise UpCloudClientError(
            f"Failed to read keyring value for {username}. Ensure that the value saved to the system keyring is correct."
        ) from None


class Credentials:
    """
    Class for handling UpCloud API credentials.
    """

    def __init__(self, username: str = None, password: str = None, token: str = None):
        """
        Initializes the Credentials object with username, password and/or token. Use `parse` method to read credentials from environment variables or keyring.
        """
        self._username = username
        self._password = password
        self._token = token

    @property
    def authorization(self) -> str:
        """
        Returns the authorization header value based on the provided credentials.
        """
        if self._token:
            return f"Bearer {self._token}"

        credentials = f"{self._username}:{self._password}".encode()
        encoded_credentials = base64.b64encode(credentials).decode()
        return f"Basic {encoded_credentials}"

    @property
    def dict(self) -> dict:
        """
        Returns the credentials as a dictionary.
        """
        return {
            "username": self._username,
            "password": self._password,
            "token": self._token,
        }

    @property
    def is_defined(self) -> bool:
        """
        Checks if the credentials are defined.
        """
        return bool(self._username and self._password or self._token)

    def _read_from_env(self):
        if not self._username:
            self._username = os.getenv(ENV_KEY_USERNAME)
        if not self._password:
            self._password = os.getenv(ENV_KEY_PASSWORD)
        if not self._token:
            self._token = os.getenv(ENV_KEY_TOKEN)

    def _read_from_keyring(self):
        if self._username and not self._password:
            self._password = _read_keyring_value(self._username)

        if self.is_defined:
            return

        self._token = _read_keyring_value(KEYRING_TOKEN_USER)

    @classmethod
    def parse(cls, username: str = None, password: str = None, token: str = None):
        """
        Parses credentials from the provided parameters, environment variables or the system keyring.
        """
        credentials = cls(username, password, token)
        if credentials.is_defined:
            return credentials

        credentials._read_from_env()
        if credentials.is_defined:
            return credentials

        credentials._read_from_keyring()
        if credentials.is_defined:
            return credentials

        raise UpCloudClientError(
            f"Credentials not found. These must be set in configuration, via environment variables or in the system keyring ({KEYRING_SERVICE_NAME})"
        )
