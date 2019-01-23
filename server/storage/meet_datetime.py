from dataclasses import dataclass

@dataclass
class MeetDateTime:
    date: str
    time_range: str
    id: int = 0
    user_id: int = 0
