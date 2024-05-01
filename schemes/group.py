from pydantic import BaseModel
from typing import Optional

from schemes.expense import Expense

class Group(BaseModel):
    id: Optional[int]
    name: str
    participants: list[int]
    expenses: list[Expense]