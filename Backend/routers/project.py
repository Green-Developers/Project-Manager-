from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Project, User
from schemas import CreateProject
from datastructures import LinkedList  # فرض می‌کنیم که این کلاس قبلاً تعریف شده
from datetime import datetime

router = APIRouter()

@router.post("/create", response_model=CreateProject)
async def create_project(
    project: CreateProject,
    db: Session = Depends(get_db)
):
    # ایجاد پروژه جدید
    new_project = Project(
        title=project.title,
        description=project.description,
        start_date=project.start_date or datetime.utcnow(),
        end_date=project.end_date,
        owner_id=1  # فرض می‌کنیم که مالک با ID 1 است
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # اضافه کردن کارمندان به LinkedList پروژه
    if project.employees:
        employees = db.query(User).filter(User.id.in_(project.employees)).all()
        for employee in employees:
            new_project.employees.append(employee)  # اضافه کردن به LinkedList

    db.commit()

    return new_project
