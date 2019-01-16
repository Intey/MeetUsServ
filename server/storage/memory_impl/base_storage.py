from abc import ABCMeta, abstractmethod
import typing as t
from copy import deepcopy

from storage import IStorage

Object = t.TypeVar('Object')
KWargs = t.Dict[str, t.Any]


class BaseStorage(t.Generic[Object], IStorage[Object]):
    """
    Storage interface. Should be subclassed with setting
    concrete type instean `Object`:

    ```
        class UserStorage(IStorage(User)): pass
    ```
    """
    def __init__(self):
        self.items: t.Dict[int, Object] = dict()
        self.last_id = 1

    def get(self, **kwargs: KWargs) -> t.Optional[Object]:
        """
        Return object, filtered by kwargs.
        If no one match - return None.
        """
        id_ = kwargs.get('id')
        if id_ is None:
            return None
        assert isinstance(id_, int), "id should be of int type"
        return self.items.get(id_)

    def create(self, obj: Object) -> t.Optional[Object]:
        """
        Create new object.
        If creations fails - return none
        """
        result = deepcopy(obj)
        result.id = self.last_id
        self.items[self.last_id] = result
        self.last_id += 1
        return result

    def update(self, obj: Object) -> t.Optional[Object]:
        """
        Update object `obj`. `obj` should have exist
        identifier to get exist object in store and
        update it with other fields in `obj`.
        If update fails - return none.
        """
        assert self.get(id=obj.id) is not None, \
            "update object should exists in storage"
        return None

    def all(self, **kwargs: KWargs) -> t.List[Object]:
        """
        Find objects.
        If no kwargs pass, returns all
        """
        for item in self.items:
            pass # todo: search for a each key and val of item
        return self.items
