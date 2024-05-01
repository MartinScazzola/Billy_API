from pydantic import BaseModel
from typing import Optional

from schemes.expense import Expense

class CompleteGroup(BaseModel):
    id_group: Optional[int]
    name: str
    participants: list[int]

class Group(BaseModel):
    id_group: Optional[int]
    name: str