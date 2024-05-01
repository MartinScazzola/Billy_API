from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.group import groups, group_expenses, group_participants
from schemes.group import CompleteGroup, Group
from schemes.expense import Expense

group = APIRouter()

@group.get('/groups', response_model=List[Group], tags=["Groups"])
def get_groups():
    return conn.execute(groups.select()).fetchall()

@group.post('/groups', response_model=Group, tags=["Groups"])
def create_group(group: CompleteGroup):
    print(group)
    new_group = {"name": group.name}
    result = conn.execute(groups.insert().values(new_group))
    created_group_id = result.inserted_primary_key[0]
    for participant in group.participants:
        conn.execute(group_participants.insert().values({"id_group": created_group_id, "id_user": participant}))
    new_group["id_group"] = created_group_id
    return new_group

# @group.get('/users/{id}', response_model=User, tags=["Users"])
# def get_user(id:str):
#     return conn.execute(users.select().where(users.c.id == id)).first()

# @group.delete('/users/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Users"])
# def delete_user(id:str):
#     result = conn.execute(users.delete().where(users.c.id == id))
#     return Response(status_code=HTTP_204_NO_CONTENT)

# @group.put('/users/{id}', response_model=User, tags=["Users"])
# def update(id:str, user: User):
#     result = conn.execute(users.update().values(name = user.name, email = user.email).where(users.c.id ==id))
#     return conn.execute(users.select().where(users.c.id == id)).first()

     