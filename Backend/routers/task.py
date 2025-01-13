from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Backend.database import get_db
from Backend.models import Task, Project, User
from Backend.schemas import TaskCreate, TaskResponse, TaskBase
from Backend.auth.auth_handler import get_current_active_user
from sqlalchemy import and_
from typing import List


router = APIRouter()


@router.post("/{project_id}/tasks", response_model=TaskResponse)
async def create_task(
    project_id: int, 
    task: TaskCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    project = db.query(Project).filter(and_(Project.id == project_id, Project.owner_id == current_user.id)).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    new_task = Task(
        name=task.name,
        description=task.description,
        start_date=task.start_date,
        end_date=task.end_date,
        project_id=project_id,
        employee_id=task.employee_id,
        status=task.status 
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task



@router.get("/{project_id}/tasks", response_model=List[TaskResponse])
async def get_project_tasks(
    project_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    tasks = db.query(Task).filter(Task.project_id == project_id).all()
    return tasks


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int, 
    task: TaskBase, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    db_project = db.query(Project).filter(Project.id == db_task.project_id).first()
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    
    if current_user.id != db_project.owner_id and current_user.id != db_task.employee_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to update this task"
        )

    db_task.name = task.name
    db_task.description = task.description
    db_task.start_date = task.start_date
    db_task.end_date = task.end_date
    db_task.employee_id = task.employee_id
    db_task.status = task.status 

    db.commit()
    db.refresh(db_task)
    return db_task



@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    db_project = db.query(Project).filter(Project.id == db_task.project_id).first()
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    # بررسی اینکه کاربر مدیر پروژه است
    if current_user.id != db_project.owner_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the project owner can delete tasks"
        )

    db.delete(db_task)
    db.commit()