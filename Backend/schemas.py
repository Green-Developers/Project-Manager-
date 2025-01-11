from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str | None = None

class UserInDB(UserResponse):
    hashed_password: str


class CreateProject(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: datetime
    employees: Optional[List[int]] = []

    class Config:
        orm_mode = True


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_date: datetime
    end_date: datetime
    owner_id: int
    employees: List[int]

    class Config:
        orm_mode = True
