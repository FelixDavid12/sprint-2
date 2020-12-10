from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel):
    id_user: int = 0
    name: str
    surname: str
    national_id: int
    email: str
    phone: int


generator_id_user = {"id_user": 0}

database_users = Dict[str, UserInDB]
database_users = {
    "a": UserInDB(**{"id_user": 1, "name": "a", "surname": "a.sur", "national_id": 1, "email": "a@a.com", "phone": 1}),
    "b": UserInDB(**{"id_user": 2, "name": "b", "surname": "b.sur", "national_id": 2, "email": "b@b.com", "phone": 2}),
}


def get_user(name: str):
    if name in database_users.keys():
        return database_users[name]
    else:
        return None


def create_user(user: UserInDB):
    generator_id_user["id_user"] = generator_id_user["id_user"] + 1
    user.id_user = generator_id_user["id_user"]
    database_users[user.name] = user
