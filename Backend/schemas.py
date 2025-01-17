from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


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
    status: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: datetime
    employees: Optional[List[int]] = []

    class Config:
        orm_mode = True


class ProjectResponse(BaseModel):
    id: int
    title: str
    status: Optional[str]
    start_date: datetime
    end_date: datetime
    owner_id: int
    employees: List[int]

    class Config:
        orm_mode = True

# تعریف Enum برای وضعیت تسک


class TaskStatus(str, Enum):
    TO_DO = "to do"
    DOING = "doing"
    DONE = "done"


class TaskBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    employee_id: int
    status: TaskStatus = TaskStatus.TO_DO  # مقدار پیش‌فرض


class TaskCreate(TaskBase):
    project_id: int


class TaskResponse(TaskBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True