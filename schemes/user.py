from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id_user: Optional[int]
    name: Optional[str]
    email: str