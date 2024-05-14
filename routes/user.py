from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from typing import List
from models.user import users
from routes.group import get_group
from schemes.group import Group
from schemes.user import User
from models.group import groups, group_participants
from sqlalchemy.sql.expression import select

user = APIRouter()

@user.get('/users', response_model=List[User], tags=["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post('/users', response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    result = conn.execute(users.insert().values(new_user))
    created_user_id = result.inserted_primary_key[0]
    new_user["id_user"] = created_user_id # Agregar el ID generado a la respuesta
    return new_user

@user.get('/users/{id}', response_model=User, tags=["Users"])
def get_user(id:str):
    return conn.execute(users.select().where(users.c.id_user == id)).first()

@user.delete('/users/{id}', status_code= status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id:str):
    result = conn.execute(users.delete().where(users.c.id_user == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/{id}', response_model=User, tags=["Users"])
def update(id:str, user: User):
    result = conn.execute(users.update().values(name = user.name, email = user.email).where(users.c.id_user ==id))
    return conn.execute(users.select().where(users.c.id_user == id)).first()

@user.get('/users/{id}/groups', response_model=List[Group], tags=["Users"])
def get_user_groups(id:str):
    group_ids =  conn.execute(select(group_participants.c.id_group).where(group_participants.c.id_user == id))
    user_groups = []
    for group_id in group_ids:
        user_groups.append(get_group(group_id[0]))
    return user_groups