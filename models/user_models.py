from pydantic import BaseModel


class UserIn(BaseModel):
    id_user: int
    name: str
    surname: str
    national_id: int
    email: str
    phone: int


class UserOut(BaseModel):
    id_user: int
    name: str
    surname: str
    national_id: int
    email: str
    phone: int
