from logging import getLogger
from storage import UserStorage, User

LOGGER = getLogger(__name__)

STORAGE = UserStorage()


def get(id):
    LOGGER.info('get user api')
    return STORAGE.get_user(id=id)

def search():
    LOGGER.info('search user api')
    return STORAGE.all()


def post(body):
    LOGGER.info('post user api')
    user = User(**body['user'])
    return STORAGE.save_user(user)


def put(id, body):
    LOGGER.info('put user api')
    user = User(id=id, **body['user'])
    return STORAGE.save_user(user)
