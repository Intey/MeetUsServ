from dataclasses import dataclass


@dataclass
class Meet:
    date: str
    timeRange: str
    id: int = 0
    user_id: int = 0
