from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Expense(BaseModel):
    id_expense: Optional[int]
    name: str
    amount: int
    currency: str
    date: datetime