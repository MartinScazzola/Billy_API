from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Expense(BaseModel):
    id: Optional[int]
    name: str
    amount: int
    date: datetime