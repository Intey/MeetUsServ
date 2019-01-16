import typing as t
from storage.istorage import IStorage
from storage.user import User
from storage.meet import Meet

def get_meets_for_user(self, user_id: int,
                       user_store: IStorage[Meet],
                       meet_store: IStorage[Meet]) -> t.List[Meet]:
    # IUserStorage.get_meets_for_user(self, user_id)
    user = user_store.get(user_id)
    if user is None:
        return []
    return meet_store.all(user_id=user_id)

    return self.meets.get(user_id)

def create_meets_for_user(self, user_id: int, meets: t.List[Meet]) -> t.List[Meet]:
    IUserStorage.create_meets_for_user(self, user_id, meets)
    for meet in meets:
        meet_ = deepcopy(meet)
        meet_.id = self.last_meet_id
        self.last_meet_id += 1
        if self.meets.get(user_id) is None:
            self.meets[user_id] = []
        self.meets[user_id].append(meet_)
    LOGGER.debug(self.meets)
    return self.meets[user_id]



