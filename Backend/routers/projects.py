from fastapi import Depends, HTTPException, status, APIRouter 
from database import get_db
from sqlalchemy.orm import Session
from models import Project, User
from schemas import Project, ProjectCreate
from auth.auth_handler import get_current_active_user
from sqlalchemy import and_


router = APIRouter()


@router.post("/projects/add", response_model=ProjectCreate)
async def add_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    new_project = Project(title=project.title, startDate=project.startDate, endDate=project.endDate, status=project.status,manager_id=current_user.id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@router.get("/projects/view", response_model=list[Project])
async def view_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(Project).all()


@router.get("/projects/view/{project_id}", response_model=Project)
async def view_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


@router.put("/projects/update/{project_id}", response_model=Project)
async def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_project = db.query(Project).filter(and_(Project.id == project_id, Project.manager_id == current_user.id)).first()
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    db_project.title = project.title
    db_project.startDate = project.startDate
    db_project.endDate = project.endDate
    db_project.status = project.status
    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/projects/delete/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_project = db.query(Project).filter(and_(Project.id == project_id, Project.manager_id == current_user.id)).first()
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    db.delete(db_project)
    db.commit()




