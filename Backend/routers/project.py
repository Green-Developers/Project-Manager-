from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_
from database import get_db
from models import Project, User
from schemas import CreateProject, ProjectResponse
from auth.auth_handler import get_current_active_user

router = APIRouter()

@router.post("/projects/create", response_model=ProjectResponse)
async def create_project(
    project: CreateProject,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # ایجاد پروژه جدید
    new_project = Project(
        title=project.title,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date,
        owner_id=current_user.id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # اضافه کردن کارمندان به پروژه
    if project.employees:
        employees = db.query(User).filter(User.id.in_(project.employees)).all()
        new_project.employees.extend(employees)

    db.commit()
    return new_project


@router.get("/projects", response_model=list[ProjectResponse])
async def view_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(Project).all()


@router.get("/projects/{project_id}", response_model=ProjectResponse)
async def view_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


@router.put("/projects/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: int,
    project: CreateProject,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_project = db.query(Project).filter(and_(Project.id == project_id, Project.owner_id == current_user.id)).first()
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    db_project.title = project.title
    db_project.description = project.description
    db_project.start_date = project.start_date
    db_project.end_date = project.end_date

    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_project = db.query(Project).filter(and_(Project.id == project_id, Project.owner_id == current_user.id)).first()
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    db.delete(db_project)
    db.commit()
