"""
Storage implementation in memory
"""

import typing as t
from copy import deepcopy

from storage.user import IUserStorage, User


class MemoryUserStorage(IUserStorage):
    """
    Contains users in memory. When server stops - all users will be lost
    """
    def __init__(self):
        self.users: t.Dict[User] = dict()
        self.last_id = 1

    def get_user(self, **kwargs: dict) -> User:
        IUserStorage.get_user(self, **kwargs)
        id_ = kwargs.get('id')
        if id_ is not None:
            return self.users[id_]
        else:
            return None

    def save_user(self, user: User, **kwargs) -> bool:
        IUserStorage.save_user(self, user, **kwargs)
        found = self.users.get(user.id)
        result = None
        if found:
            found.username = user.username
            result = found
        else:
            result = deepcopy(user)
            result.id = self.last_id
            self.users[self.last_id] = result
            self.last_id += 1
        return result

    def all(self, **kwargs) -> t.List[User]:
        return list(self.users.values())
