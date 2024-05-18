from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.group import groups, group_expenses, group_participants
from schemes.group import CompleteGroup, Group
from schemes.expense import Expense

expense = APIRouter()


@expense.post('/expenses', response_model=Expense, tags=["Expenses"])
def create_expense(expense: Expense):
    new_expense = {"name": expense.name, "id_group": expense.id_group, "id_user": expense.id_user, "amount": expense.amount, "currency": expense.currency}
    result = conn.execute(group_expenses.insert().values(new_expense))
    created_expense_id = result.inserted_primary_key[0]
    # for participant in group.participants:
    #     conn.execute(group_participants.insert().values({"id_group": created_group_id, "id_user": participant}))
    new_expense["id_expense"] = created_expense_id
    return new_expense

@expense.get('/expenses', response_model=List[Expense], tags=["Expenses"])
def get_expenses():
    return conn.execute(group_expenses.select()).fetchall()
