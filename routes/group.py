from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT
from schemes.user import User
from config.db import conn
from typing import List
from models.user import users
from models.group import groups, group_expenses, group_participants
from schemes.group import CompleteGroup, Group
from schemes.expense import Expense
from config.middleware import get_db

group = APIRouter()

@group.get('/groups', response_model=List[Group], tags=["Groups"])
def get_groups(db: Session = Depends(get_db)):
    return db.execute(groups.select()).fetchall()

@group.post('/groups', response_model=Group, tags=["Groups"])
def create_group(group: CompleteGroup, db: Session = Depends(get_db)):
    new_group = {"name": group.name}
    result = db.execute(groups.insert().values(new_group))
    created_group_id = result.inserted_primary_key[0]
    for participant in group.participants:
        db.execute(group_participants.insert().values({"id_group": created_group_id, "id_user": participant}))
    new_group["id_group"] = created_group_id
    return new_group

@group.post('/groups/{id}/users', response_model=Group, tags=["Groups"])
def add_user_to_group(id_user:str, id_group:str, db: Session = Depends(get_db)):
    db.execute(group_participants.insert().values({"id_group": id_group, "id_user": id_user}))
    return get_group(id_group, db)

@group.get('/groups/{id}/users', response_model=List[User], tags=["Groups"])
def get_users_from_group(id:str, db: Session = Depends(get_db)):
    users_in_group = db.execute(group_participants.select().where(group_participants.c.id_group == id)).fetchall()
    user_list = []
    for user in users_in_group:
        user_list.append(db.execute(users.select().where(users.c.id_user == user[0])).first())
    return user_list

@group.delete('/groups/{id}/users', status_code= status.HTTP_204_NO_CONTENT, tags=["Groups"])
def remove_user_from_group(id_user:str, id_group:str,db: Session = Depends(get_db)):
    result = db.execute(group_participants.delete().where(group_participants.c.id_user == id_user, group_participants.c.id_group == id_group))
    return Response(status_code=HTTP_204_NO_CONTENT)

@group.get('/groups/{id}', response_model=Group, tags=["Groups"])
def get_group(id:str,db: Session = Depends(get_db)):
    return db.execute(groups.select().where(groups.c.id_group == id)).first()

@group.delete('/groups/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Groups"])
def delete_group(id:str,db: Session = Depends(get_db)):
    result = db.execute(groups.delete().where(groups.c.id_group == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

# @group.put('/users/{id}', response_model=User, tags=["Users"])
# def update(id:str, user: User):
#     result = conn.execute(users.update().values(name = user.name, email = user.email).where(users.c.id ==id))
#     return conn.execute(users.select().where(users.c.id == id)).first()

     