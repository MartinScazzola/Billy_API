from fastapi import APIRouter, Depends, HTTPException

from repository.queries.user_queries import *

from control.models.user import *

from constants import *


router = APIRouter()


@router.post("/user", tags=["Users"])
def api_create_user(user: UserCreateRequest):
    #try:
    user_db = create_user(user.username, user.name, user.surname, user.password, user.email)
        
    return generate_user_response(user_db)
    #except InsertUserFailed as e:
    #    raise HTTPException(status_code=BAD_REQUEST, detail=str(error)) from error