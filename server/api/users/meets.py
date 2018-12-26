from logging import getLogger
from storage import UserStorage, User

LOGGER = getLogger(__name__)

STORAGE = UserStorage()


def post(uid, body):
    result = STORAGE.create_meets_for_user(id, body['meets'])
    return result


def search(uid):
    result = STORAGE.get_meets_for_user(id)
    return result
