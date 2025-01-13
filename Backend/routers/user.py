from fastapi import APIRouter, Depends

from Backend.auth.auth_handler import get_current_active_user
from Backend.schemas import UserResponse
from Backend.models import User

router = APIRouter()


@router.get("me/", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
