from logging import getLogger
from storage import UserStorage, User, Meet

LOGGER = getLogger(__name__)

STORAGE = UserStorage()


def post(uid: int, body: dict):
    meets = []
    for meet in body['meets']:
        print(meet)
        meets.append(Meet(date=meet['date'], timeRange=meet['timeRange']))

    result = STORAGE.create_meets_for_user(uid, meets)
    return result


def search(uid):
    result = STORAGE.get_meets_for_user(uid)
    return result
