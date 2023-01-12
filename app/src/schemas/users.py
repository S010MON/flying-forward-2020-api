from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    old_password: str
    new_password: str


class User(UserBase):
    id: int
    disabled: bool
    failed_attempts: int

    class Config:
        orm_mode = True
