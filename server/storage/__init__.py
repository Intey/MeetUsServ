"""
Interface realization for current project
"""

from .memory_impl.user import MemoryUserStorage as __impl
from .user import User
from .user import Meet

UserStorage = __impl
