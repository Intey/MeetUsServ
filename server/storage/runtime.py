from .user import User
from .meet import Meet
from .istorage import IStorage
from .memory_impl.user import MemoryUserStorage as __mus
from .memory_impl.meet import MemoryMeetStorage as __mms

user_store: IStorage[User] = __mus()
meet_store: IStorage[Meet] = __mms()
