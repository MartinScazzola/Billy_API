from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Expense(BaseModel):
    id_expense: Optional[int]
    id_group: int
    id_user: int
    name: str
    amount: int
    currency: str
    liquidated: bool
    participants: List[int]
    expense_distribution: List[int]
