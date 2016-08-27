import abc
import uuid


class AbstractStore(object):
    """Base store"""

    __metaclass__ = abc.ABCMeta
    model_class = None

    def create(self, **kwargs):
        _id = uuid.uuid4().hex
        obj = self.model_class(id=_id, **kwargs)
        self.put(obj)
        return obj

    @abc.abstractmethod
    def get(self, obj_id):
        pass

    @abc.abstractmethod
    def put(self, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, obj_id):
        pass

    @abc.abstractmethod
    def all(self):
        pass


class MemoryStore(AbstractStore):
    def __init__(self, *args, **kwargs):
        self._stores = {}

    def get(self, obj_id):
        return self._stores[obj_id]

    def put(self, obj):
        self._stores[obj.id] = obj

    def delete(self, obj_id):
        del self._stores[obj_id]

    def all(self):
        return self._stores.values()
