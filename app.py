from fastapi import FastAPI
from routes.user import user
from routes.group import group
from routes.expense import expense
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user)
app.include_router(group)
app.include_router(expense)


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)