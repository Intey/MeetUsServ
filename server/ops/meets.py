import typing as t
from storage.istorage import IStorage
from storage.user import User
from storage.meet import Meet
from storage.meet_datetime import MeetDateTime as MeetTime


def create_meet(user_store: IStorage[User], meet_store: IStorage[Meet],
                name: str, description: str):

    meet = Meet(name, description)
    meet = meet_store.create(meet)


# with separated storage
def add_time_ranges_for_meet(user_store: IStorage[User], meet_store: IStorage[Meet],
                             meet_times_store: IStorage[MeetTime],
                             meet_id: int, user_id: int, times: t.List[MeetTime]) -> t.List[MeetTime]:
    meet = meet_store.get(id=meet_id)
    result = []
    for time in times:
        obj = meet_times_store.create(**time, meet_id=meet_id, user_id=user_id)
        result.append(obj)
    return result


#with meet_store
def add_time_ranges_for_meet(user_store: IStorage[User], meet_store: IStorage[Meet],
                             meet_id: int, user_id: int, times: t.List[MeetTime]) -> t.List[MeetTime]:
    meet = meet_store.get(id=meet_id)
    results = meet_store.add_times_for_meet(id=meet_id, times=times, user_id=user_id)
    return results


#with meet object
def add_time_ranges_for_meet(user_store: IStorage[User], meet_store: IStorage[Meet],
                             meet_id: int, user_id: int, times: t.List[MeetTime]) -> t.List[MeetTime]:
    meet = meet_store.get(id=meet_id)
    # meet should know of how to save times
    # FALSE
    results = meet.add_times_for_meet(times=times, user_id=user_id)
    return results


def create_meets_for_user(user_store: IStorage[User], meet_store: IStorage[Meet],
                          user_id: int, meets: t.List[Meet]) -> t.List[Meet]:
    if user_store.get(id=user_id) is None:
        return dict(error=f"user {uid} doesn't exist")

    results = []
    for meet in meets:
        meet_ = Meet(date=meet['date'], timeRange=meet['timeRange'])
        meet_.user_id = user_id
        new_meet = meet_store.create(meet_)
        results.append(new_meet)

    return results

