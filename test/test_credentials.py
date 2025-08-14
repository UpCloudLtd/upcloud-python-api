import keyring

from upcloud_api import Credentials


class DictBackend(keyring.backend.KeyringBackend):
    priority = 1

    def __init__(self, secrets=None):
        super().__init__()
        self._secrets = secrets or {}

    def set_password(self, servicename, username, password):
        pass

    def get_password(self, servicename, username):
        return self._secrets.get(servicename, {}).get(username)

    def delete_password(self, servicename, username):
        pass


class TestCredentials:
    def test_precedence(self, monkeypatch):
        param_basic = 'Basic cGFyYW1fdXNlcjpwYXJhbV9wYXNz'
        param_bearer = 'Bearer param_token'
        env_basic = 'Basic ZW52X3VzZXI6ZW52X3Bhc3M='
        env_bearer = 'Bearer env_token'
        keyring_basic = 'Basic ZW52X3VzZXI6a2V5cmluZ19wYXNz'
        keyring_bearer = 'Bearer keyring_token'

        backend = DictBackend(
            {
                "UpCloud": {
                    "env_user": "keyring_pass",
                    "": "keyring_token",
                }
            }
        )
        keyring.set_keyring(backend)

        credentials = Credentials.parse()
        assert credentials.authorization == keyring_bearer

        monkeypatch.setenv("UPCLOUD_USERNAME", 'env_user')

        credentials = Credentials.parse()
        assert credentials.authorization == keyring_basic

        monkeypatch.setenv("UPCLOUD_PASSWORD", 'env_pass')

        credentials = Credentials.parse(username='param_user', password='param_pass')
        assert credentials.authorization == param_basic

        credentials = Credentials.parse()
        assert credentials.authorization == env_basic

        monkeypatch.setenv("UPCLOUD_TOKEN", 'env_token')
        credentials = Credentials.parse(username='param_user', password='param_pass')
        assert credentials.authorization == param_basic

        credentials = Credentials.parse()
        assert credentials.authorization == env_bearer

        credentials = Credentials.parse(token='param_token')
        assert credentials.authorization == param_bearer
