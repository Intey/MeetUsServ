import typing as t
from storage.istorage import IStorage
from storage.user import User
from storage.meet import Meet
from storage.meet_datetime import MeetDateTime as MeetTime
from storage.storage import Storage
from .exception import OperationException


def create_meet(user_store: IStorage[User], meet_store: IStorage[Meet],
                name: str, description: str):
    meet = Meet(name, description)
    meet = meet_store.create(meet)
    return meet


# with separated storage
def add_time_ranges_for_meet(storage: Storage,
                             meet_id: int, user_id: int,
                             times: t.List[MeetTime]) -> t.List[MeetTime]:
    if storage.user_store.get(id=user_id) is None:
        raise OperationException(f"user {user_id} doesn't exist")
    created_times = storage.create_time_for_meet(meet_id, user_id, times)
    return created_times




def create_meets_for_user(user_store: IStorage[User], meet_store: IStorage[Meet],
                          user_id: int, meets: t.List[Meet]) -> t.List[Meet]:
    if user_store.get(id=user_id) is None:
        raise OperationException(f"user {user_id} doesn't exist")

    results = []
    for meet in meets:
        meet_ = Meet(date=meet['date'], timeRange=meet['timeRange'])
        meet_.user_id = user_id
        new_meet = meet_store.create(meet_)
        results.append(new_meet)

    return results


def get_meets_of_user(user_store: IStorage[User], meet_store: IStorage[Meet],
                      user_id: int):
    if user_store.get(id=user_id) is None:
        raise OperationException(f"user {user_id} doesn't exist")
    result = meet_store.all(user_id=user_id)
    return result

