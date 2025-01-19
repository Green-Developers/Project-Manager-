from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from Backend.database import get_db
from Backend.models import Project, User
from Backend.schemas import CreateProject, ProjectResponse, AddEmployeesRequest, UserResponse
from Backend.auth.auth_handler import get_current_active_user
from datastructures import MinHeap
router = APIRouter()


@router.post("/create", response_model=ProjectResponse)
async def create_project(
    project: CreateProject,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
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

    if project.employees:
        employees = db.query(User).filter(User.id.in_(project.employees)).all()
        new_project.employees.extend(employees)

    db.commit()
    return new_project


@router.get("/", response_model=list[ProjectResponse])
async def view_projects(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_active_user)
):
    return db.query(Project).filter(
        or_(
            Project.owner_id == current_user.id,
            Project.employees.any(id=current_user.id) 
        )
    ).all()


@router.get("/project/{project_id}", response_model=ProjectResponse)
async def view_project(
    project_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_active_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"
        )

    is_owner = project.owner_id == current_user.id
    is_employee = any(user.id == current_user.id for user in project.employees)

    if not (is_owner or is_employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to access this project"
        )

    return project



@router.put("/project/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: int,
    project: CreateProject,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_project = db.query(Project).filter(
        and_(Project.id == project_id, Project.owner_id == current_user.id)
    ).first()
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"
        )

    db_project.title = project.title
    db_project.description = project.description
    db_project.start_date = project.start_date
    db_project.end_date = project.end_date

    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/project/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_active_user)
):
    db_project = db.query(Project).filter(Project.id == project_id).first()

    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"
        )

    if db_project.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to delete this project"
        )

    db.delete(db_project)
    db.commit()


@router.post("/add_employees/{project_id}", response_model=ProjectResponse)
async def add_employees_to_project(
    project_id: int, 
    employees: AddEmployeesRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"
        )

    if project.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to add employees to this project"
        )

    employees_to_add = db.query(User).filter(User.id.in_(employees)).all()

    if len(employees_to_add) != len(employees):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="One or more employees not found"
        )

    project.employees.extend(employees_to_add)

    db.commit()
    db.refresh(project)

    return project

@router.get("/{project_id}/employees_sorted", response_model=list[UserResponse])
async def get_sorted_employees(
    project_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_active_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Project not found"
        )

    if project.owner_id != current_user.id and not any(user.id == current_user.id for user in project.employees):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to view employees of this project"
        )

    employees = project.employees

    heap = MinHeap()
    for employee in employees:
        heap.insert(employee)

    sorted_employees = heap.sorted()

    return sorted_employees
