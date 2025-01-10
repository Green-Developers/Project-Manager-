from fastapi import APIRouter, Body
from Backend.schema._input import RegisterInput
from Backend.db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from Backend.oprations.users import Usersoprations
from fastapi import Depends

router = APIRouter()


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
async def login(): ...


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
