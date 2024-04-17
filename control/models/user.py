from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    surname: str
    email: str

class UserCreateRequest(BaseModel):
    username: str
    name: str
    surname: str
    password: str
    email:str

def generate_user_response(user_db):
    return UserResponse(
        id = user_db.id,
        username = user_db.username,
        name = user_db.name,
        surname = user_db.surname,
        email = user_db.email
    )