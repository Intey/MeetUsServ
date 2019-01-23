from logging import getLogger
from storage import User, Meet

from runtime_ops import create_meets_for_user

LOGGER = getLogger(__name__)


def post(uid: int, body: dict):
    meets = body['meets']
    create_meets_for_user(uid, meets)


def search(uid: int):
    result = meet_store.all(user_id=uid)
    return result
