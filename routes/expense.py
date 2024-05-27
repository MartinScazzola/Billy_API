from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT
from config.middleware import get_db
from typing import List
from models.group import (
    groups,
    group_expenses,
    group_participants,
    expense_participants,
)
from schemes.group import CompleteGroup, Group
from schemes.expense import Expense

expense = APIRouter()


@expense.post("/expenses", response_model=Expense, tags=["Expenses"])
def create_expense(expense: Expense,db: Session = Depends(get_db)):
    new_expense = {
        "name": expense.name,
        "id_group": expense.id_group,
        "id_user": expense.id_user,
        "amount": expense.amount,
        "currency": expense.currency,
        "liquidated": False,
    }
    result = db.execute(group_expenses.insert().values(new_expense))
    created_expense_id = result.inserted_primary_key[0]
    new_expense["id_expense"] = created_expense_id

    for i,id_participant in enumerate(expense.participants):
        conn.execute(expense_participants.insert().values({"id_expense": created_expense_id, "id_user": id_participant, "amount": expense.expense_distribution[i]}))

    new_expense["participants"] = expense.participants
    new_expense["expense_distribution"] = expense.expense_distribution
    return new_expense


@expense.get("/expenses", response_model=List[Expense], tags=["Expenses"])
def get_expenses(db: Session = Depends(get_db)):
    result_group_expenses = db.execute(group_expenses.select()).fetchall()
    expenses = []
    for expense in result_group_expenses:
        expense_dict = {
            "id_expense": expense[0],
            "id_group": expense[1],
            "id_user": expense[2],
            "amount": expense[3],
            "currency": expense[4],
            "name": expense[5],
            "liquidated": expense[6],
        }
        expense_dict["participants"] = []
        result_expense_participants = db.execute(
            expense_participants.select().where(
                expense_participants.c.id_expense == expense[0]
            )
        ).fetchall()
        for participant in result_expense_participants:
            expense_dict["participants"].append(participant[1])
        expenses.append(expense_dict)
    return expenses


@expense.delete(
    "/expenses/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Expenses"]
)
def delete_expense(id: str, db: Session = Depends(get_db)):
    db.execute(group_expenses.delete().where(group_expenses.c.id_expense == id))
    db.execute(
        expense_participants.delete().where(expense_participants.c.id_expense == id)
    )
    return Response(status_code=HTTP_204_NO_CONTENT)

@expense.put("/expenses/{id}", response_model=Expense, tags=["Expenses"])
def updateExpense(id:str, expense: Expense, db: Session = Depends(get_db)):
    result = db.execute(
        group_expenses.update()
        .values(
            id_group=expense.id_group,
            id_user=expense.id_user,
            name=expense.name,
            amount=expense.amount,
            currency=expense.currency,
            liquidated=expense.liquidated,
        )
        .where(group_expenses.c.id_expense == id)
    )
    expense_updated = db.execute(group_expenses.select().where(group_expenses.c.id_expense == id)).first()
    expense_updated = { "id_expense": expense_updated[0], "id_group": expense_updated[1], "id_user": expense_updated[2], "amount": expense_updated[3], "currency": expense_updated[4], "name": expense_updated[5], "liquidated": expense_updated[6]
    }
    expense_updated["participants"] = expense.participants
    return expense_updated
