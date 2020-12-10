from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    surname: str
    national_id: int
    email: str
    phone: int


class UserOut(BaseModel):
    name: str
    surname: str
    national_id: int
    email: str
    phone: int
