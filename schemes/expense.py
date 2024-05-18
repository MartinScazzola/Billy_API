from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Expense(BaseModel):
    id_expense: Optional[int]
    id_group: int
    id_user: int
    name: str
    amount: int
    currency: str