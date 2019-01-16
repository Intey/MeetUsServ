from logging import getLogger
from storage import User, Meet

from storage.runtime import user_store, meet_store

LOGGER = getLogger(__name__)


def post(uid: int, body: dict):
    if user_store.get(id=uid) is None:
        return dict(error=f"user {uid} doesn't exist")

    results = []
    for meet in body['meets']:
        meet_ = Meet(date=meet['date'], timeRange=meet['timeRange'])
        meet_.user_id = uid
        results.append(meet_store.create(meet_))

    return results


def search(uid: int):
    result = meet_store.all(user_id=uid)
    return result
