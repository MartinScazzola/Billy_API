from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from control.controller_user import router as router_user

tags_metadata = [
    {"name": "Users", "description": "Endpoints Users"},
]

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_user, prefix="")