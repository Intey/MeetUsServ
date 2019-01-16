from abc import ABCMeta, abstractmethod
import typing as t

Object = t.TypeVar('Object')
KWargs = t.Dict[str, t.Any]


class IStorage(t.Generic[Object], metaclass=ABCMeta):
    """
    Storage interface. Should be subclassed with setting
    concrete type instean `Object`:

    ```
        class UserStorage(IStorage[User]): pass
    ```
    """

    @abstractmethod
    def get(self, **kwargs: KWargs) -> t.Optional[Object]:
        """
        Return object, filtered by kwargs.
        If no one match - return None.
        """

    @abstractmethod
    def create(self, obj: Object) -> t.Optional[Object]:
        """
        Create new object.
        If creations fails - return none
        """

    @abstractmethod
    def update(self, obj: Object) -> t.Optional[Object]:
        """
        Update object `obj`. `obj` should have exist
        identifier to get exist object in store and
        update it with other fields in `obj`.
        If update fails - return none.
        """

    @abstractmethod
    def all(self, **kwargs: KWargs) -> t.List[Object]:
        """
        Find objects.
        If no kwargs pass, returns all
        """
