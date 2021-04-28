from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from upcloud_api import CloudManager


class UpCloudResource:
    """
    Base class for all API resources.

    ATTRIBUTES is used to define serialization (see: to_dict)
    and defaults (see: __init__ and _reset).

    All UpCloudResources:
    - must define ATTRIBUTES accordingly with https://www.upcloud.com/api/ (doc)
    - must have `to_dict` for JSON serialization
    - must have `_reset` for initializing and refreshing the instance with updated data
    - must call `UpCloudResource.__init__` (that uses `_reset`)
    - optionally implement `sync` for refreshing the instance with new data from API
    """

    ATTRIBUTES = {}  # subclass should define this

    cloud_manager: 'CloudManager'

    def __init__(self, **kwargs) -> None:
        """
        Create a resource object from a dict.

        Set attributes from kwargs and any missing defaults from ATTRIBUTES.
        """
        self._reset(**kwargs)

    def _reset(self, **kwargs) -> None:
        """
        Reset after repopulating from API (or when initializing).
        """
        # set object attributes from params
        for key in kwargs:
            setattr(self, key, kwargs[key])

        # set defaults (if need be) where the default is not None
        for attr in self.ATTRIBUTES:
            if not hasattr(self, attr) and self.ATTRIBUTES[attr] is not None:
                setattr(self, attr, self.ATTRIBUTES[attr])

    def sync(self):
        """
        Sync the object from the API and use the internal resource._reset to
        update fields.
        """
        raise NotImplementedError

    def to_dict(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.
        """
        return {attr: getattr(self, attr) for attr in self.ATTRIBUTES if hasattr(self, attr)}
