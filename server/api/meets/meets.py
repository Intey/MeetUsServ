from logging import getLogger
from storage import User, Meet

from runtime_ops import create_meets_for_user, get_meets_of_user
from ops.exception import OperationException

LOGGER = getLogger(__name__)


def post(uid: int, body: dict):
    meets = body['meets']
    create_meets_for_user(uid, meets)


def search(uid: int):
    try:
        return get_meets_of_user(uid)
    except OperationException as e:
        LOGGER.info(f"Exception in get_meets_of_user({uid}): {e.message}")
        return e.message, 404

