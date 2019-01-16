from logging import getLogger
from storage.runtime import user_store
from storage import User

LOGGER = getLogger(__name__)

def get(id):
    LOGGER.info('get user api')
    return user_store.get_user(id=id)

def search():
    LOGGER.info('search user api')
    return user_store.all()


def post(body):
    LOGGER.info('post user api')
    user = User(**body['user'])
    return user_store.save_user(user)


def put(id, body):
    LOGGER.info('put user api')
    user = User(id=id, **body['user'])
    return user_store.save_user(user)
