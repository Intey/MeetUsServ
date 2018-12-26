
from abc import ABCMeta, abstractmethod
import typing as t
from logging import getLogger
from dataclasses import dataclass

LOGGER = getLogger(__name__)


@dataclass
class User:
    username: str
    id: int = 0


class IUserStorage(metaclass=ABCMeta):
    """
    User storage interface
    """
    @abstractmethod
    def get_user(self, **kwargs) -> User:
        """
        Return user, filtered by kwargs
        """
        LOGGER.info("get user called")

    @abstractmethod
    def save_user(self, user: User, **kwargs) -> bool:
        """
        Update user data
        """
        LOGGER.info("save user called")

    @abstractmethod
    def all(self, **kwargs) -> t.List[User]:
        """
        Return all users
        """
        LOGGER.info("all user called")
