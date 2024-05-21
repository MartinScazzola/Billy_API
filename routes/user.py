from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT
from starlette.status import HTTP_404_NOT_FOUND
from config.db import conn
from typing import List
from models.user import users
from routes.group import get_group
from schemes.group import Group
from schemes.user import User
from models.group import groups, group_participants
from sqlalchemy.sql.expression import select
from config.middleware import get_db

user = APIRouter()

@user.get('/users', response_model=List[User], tags=["Users"])
def get_users(db: Session = Depends(get_db)):
    return db.execute(users.select()).fetchall()

@user.post('/users', response_model=User, tags=["Users"])
def create_user(user: User, db: Session = Depends(get_db)):
    new_user = {"name": user.name, "email": user.email}
    result = db.execute(users.insert().values(new_user))
    created_user_id = result.inserted_primary_key[0]
    new_user["id_user"] = created_user_id
    return new_user

@user.get('/users/{id}', response_model=User, tags=["Users"])
def get_user(id: str, db: Session = Depends(get_db)):
    return db.execute(users.select().where(users.c.id_user == id)).first()

@user.get('/userid', response_model=User, tags=["Users"])
def get_user_id_from_email(email: str, db: Session = Depends(get_db)):
    users_list = db.execute(users.select()).fetchall()
    for user in users_list:
        if user.email == email:
            return user
    return Response(status_code=HTTP_404_NOT_FOUND)

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: str, db: Session = Depends(get_db)):
    db.execute(users.delete().where(users.c.id_user == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/{id}', response_model=User, tags=["Users"])
def update_user(id: str, user: User, db: Session = Depends(get_db)):
    db.execute(users.update().values(name=user.name, email=user.email).where(users.c.id_user == id))
    return db.execute(users.select().where(users.c.id_user == id)).first()

@user.get('/users/{id}/groups', response_model=List[Group], tags=["Users"])
def get_user_groups(id: str, db: Session = Depends(get_db)):
    group_ids = db.execute(select(group_participants.c.id_group).where(group_participants.c.id_user == id)).fetchall()
    user_groups = [get_group(group_id[0], db) for group_id in group_ids]
    return user_groups