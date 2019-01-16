from storage import Meet, User, IStorage
from .memory_impl.user import MemoryUserStorage
from .memory_impl.meet import MemoryMeetStorage

user_store: IStorage[User] = MemoryUserStorage
meet_store: IStorage[Meet] = MemoryMeetStorage
