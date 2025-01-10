from fastapi import APIRouter, Body, HTTPException, Depends 
from Backend.db.engine import get_db, get_session
from Backend.schema._input import RegisterInput
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from Backend.oprations.users import Usersoprations
from Backend.db.models import User
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/register")
async def register(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: RegisterInput = Body(),
):
    user = await Usersoprations(db_session).create(
        username=data.username, email=data.email, password=data.password
    )
    return user


@router.post("/login")
async def login(
    request: LoginRequest, 
    session: AsyncSession = Depends(get_session)
):
    query = select(User).where(User.username == request.username,
                               User.password == request.password)
    result = await session.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(
            status_code=401, detail="Invalid username or password"
        )
    return {"message": "Login successful"}


@router.get("/{username}")
async def get_users_profile(
    username: str,
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    user_profile = await Usersoprations(db_session).get_user_by_username(
        username=username
    )

    return user_profile


@router.put("/")
async def user_update_profile(): ...
