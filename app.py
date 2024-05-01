from fastapi import FastAPI
from routes.user import user
from routes.group import group

app = FastAPI()
app.include_router(user)
app.include_router(group)
