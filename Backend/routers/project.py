from fastapi import APIRouter
from models import Project , User
from schemas import CreateProject
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from auth.auth_handler import get_current_active_user
from datetime import datetime




router = APIRouter()


# تابع ایجاد پروژه
@router.post("/create", response_model=CreateProject)
async def create_project(
    project: CreateProject,
    #current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    new_project = Project(
        title=project.title,
        description=project.description,
        start_date=project.start_date or datetime.utcnow(),  # مقدار پیش‌فرض در زمان اجرا
        end_date=project.end_date,
        #owner_id=current_user.id
        owner_id=1
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
