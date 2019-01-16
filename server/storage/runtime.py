from storage import Meet, User, IStorage
from .memory_impl.user import MemoryUserStorage
from .memory_impl.meet import MemoryMeetStorage
from .memory_impl.base_storage import BaseStorage

user_store: IStorage[User] = MemoryUserStorage()
meet_store: IStorage[Meet] = MemoryMeetStorage()
