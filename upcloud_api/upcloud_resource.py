
class UpCloudResource():

    ATTRIBUTES = {}  # subclass should define this

    def __init__(self, **kwargs):
        """
        Create a resource object from a dict.

        Set attributes from kwargs and any missing defaults from ATTRIBUTES.
        """
        self._reset(**kwargs)

    def _reset(self, **kwargs):
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
        print('muh', self.__dict__)

    def sync_from_api(self):
        """
        Sync the object from the API and use the internal resource._reset to
        update fields.
        """
        raise NotImplementedError

    def to_dict(self):
        """
        Return a dict that can be serialised to JSON and sent to UpCloud's API.
        """
        return dict(
            (attr, getattr(self, attr))
            for attr in self.ATTRIBUTES
            if hasattr(self, attr)
        )
