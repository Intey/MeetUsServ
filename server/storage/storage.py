import typing as t
from .meet_datetime import MeetDateTime

class StorageException(BaseException):
    def __init__(self, message, *args, **kwargs):
        BaseException.__init__(*args, **kwargs)
        self.message = message


class Storage:
    """
    Root storage for all entities.
    Responsibility:
        - access to storage of concrete entity
        - special case creations.

    Last resposibility is for performance sake.  When
    creating or getting coupled data it's can be faster to
    get 1 request to storage implementation.  But it is not
    prevent to get different requests in one function. This
    is about how to get coupled data - interactor should
    not know how to link objects - storage return it's
    coupled already. But Storage not declare how to process
    errors. It's just return data. If some implementation
    error has place - raise StorageException in
    implementation.
    """
    def __init__(self, user_store, meet_store, meet_times_store):
        self.user = user_store
        self.meet = meet_store
        self.meet_times = meet_times_store

    def create_time_for_meet(self, meet_id: int, user_id: int,
                             times: t.List[MeetDateTime]):
        meet = self.meet.get(id=meet_id)
        if not meet:
            return []

        result = []
        for time in times:
            obj = self.meet_times.create(**time,
                                         meet_id=meet_id,
                                         user_id=user_id)
            result.append(obj)
        return result
