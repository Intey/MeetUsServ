"""
Storage implementation in memory
"""

import typing as t
from copy import deepcopy

from storage.user import IUserStorage, User, Meet


class MemoryUserStorage(IUserStorage):
    """
    Contains users in memory. When server stops - all users will be lost
    """
    def __init__(self) -> None:
        self.users: t.Dict[int, User] = dict()
        self.meets: t.Dict[int, t.List[Meet]] = dict()
        self.last_id = 1
        self.last_meet_id = 1

    def get_user(self, **kwargs: dict) -> t.Optional[User]:
        IUserStorage.get_user(self, **kwargs)
        id_ = kwargs.get('id')
        if isinstance(id_, str):
            if id_ is not None:
                id_ = int(id_)
                return self.users[id_]['users']
        return None

    def save_user(self, user: User, **kwargs) -> t.Optional[User]:
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

    def get_meets_for_user(self, user_id: int) -> t.List[Meet]:
        IUserStorage.get_meets_for_user(self, user_id)
        user = self.users.get(user_id)
        if user is None:
            return []
        return self.meets[user_id]

    def create_meets_for_user(self, user_id: int, meets: t.List[Meet]) -> t.List[Meet]:
        IUserStorage.create_meets_for_user(self, user_id, meets)
        for meet in meets:
            meet_ = deepcopy(meet)
            meet_.id = self.last_meet_id
            self.last_meet_id += 1
            if self.meets.get(user_id) is None:
                self.meets[user_id] = []
            self.meets[user_id].append(meet_)
        return self.meets[user_id]



