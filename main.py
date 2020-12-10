from db.user_db import UserInDB
from db.user_db import create_user, get_user
from models.user_models import UserIn, UserOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()


@api.get("/user/{username}")
async def list_user(username: str):
    user_in_db = get_user(username)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out


@api.post("/user/create/")
async def add_user(user_in: UserIn):
    user_in_db = get_user(user_in.name)
    if user_in_db is None:
        create_user(user_in)
    else:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    return "Correctamente añadido el usuario " + user_in.name
