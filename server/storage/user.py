
from abc import ABCMeta, abstractmethod
import typing as t
from logging import getLogger
from dataclasses import dataclass

LOGGER = getLogger(__name__)


@dataclass
class User:
    username: str
    id: int = 0


@dataclass
class Meet:
    date: str
    timeRange: str
    id: int = 0


class IUserStorage(metaclass=ABCMeta):
    """
    User storage interface
    """
    @abstractmethod
    def get_user(self, **kwargs) -> t.Optional[User]:
        """
        Return user, filtered by kwargs
        """

    @abstractmethod
    def save_user(self, user: User, **kwargs) -> t.Optional[User]:
        """
        Update user data
        """

    @abstractmethod
    def all(self, **kwargs) -> t.List[User]:
        """
        Return all users
        """

    @abstractmethod
    def get_meets_for_user(self, user_id: int) -> t.List[Meet]:
        """
        return meets payload for user
        """

    @abstractmethod
    def create_meets_for_user(self, user_id: int, meets: t.List[Meet]) -> t.List[Meet]:
        """
        add meets data for user
        """

