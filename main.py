from db.user_db import UserInDB
from db.user_db import create_user, get_user, get_all_users
from models.user_models import UserIn, UserOut

from fastapi import FastAPI
from fastapi import HTTPException

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8081", "http://localhost:8080",
    "https://sprint-3-12.herokuapp.com"
]
api.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])


@api.get("/user/{username}")
async def list_user(username: str):
    user_in_db = get_user(username)
    if user_in_db is None:
        return "El usuario " + username + " no existe"
    user_out = UserOut(**user_in_db.dict())
    return user_out


@api.post("/user/create/")
async def add_user(user_in: UserIn):
    user_in_db = get_user(user_in.name)
    user_in = UserInDB(**user_in.dict())
    if user_in_db is None:
        create_user(user_in)
    else:
        return "El usuario " + user_in.name + " ya existe"
    return "Correctamente añadido el usuario " + user_in.name


@api.get("/users/")
async def get_users():
    users = get_all_users()
    return users
