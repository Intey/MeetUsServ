"""
Storage implementation in memory
"""

from logging import getLogger
import typing as t

from .base_storage import BaseStorage
from storage.user import User


LOGGER = getLogger(__name__)

class MemoryUserStorage(BaseStorage[User]):
    """
    Contains users in memory. When server stops - all users will be lost
    """
    def __init__(self) -> None:
        BaseStorage.__init__(self)

    def get_user(self, **kwargs: dict) -> t.Optional[User]:
        return BaseStorage.get(self, **kwargs)

    def save_user(self, user: User, **kwargs) -> t.Optional[User]:
        found = BaseStorage.get(self, **kwargs)
        result = None
        if found:
            result = BaseStorage.update(self, found)
        else:
            result = BaseStorage.create(self, user)
        return result

    def all(self, **kwargs) -> t.List[User]:
        return BaseStorage.all(self)

