from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List
from Backend.database import get_db
from Backend.models import Task, Project, User, TaskStatus
from Backend.schemas import TaskCreate, TaskResponse, TaskBase
from Backend.auth.auth_handler import get_current_active_user
from Backend.datastructures import TaskHashMap, PriorityQueue


todo_queue = PriorityQueue()
doing_queue = PriorityQueue()
done_queue = PriorityQueue()
task_map = TaskHashMap()

router = APIRouter()


@router.post("/{project_id}/tasks", response_model=TaskResponse)
async def create_task(
    project_id: int, 
    task: TaskCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    permission = db_project and db_project.owner_id == current_user.id

    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    elif not permission:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to perform this operation")
    else:
        new_task = Task(
            name=task.name,
            description=task.description,
            start_date=task.start_date,
            end_date=task.end_date,
            project_id=project_id,
            employee_id=task.employee_id,
            status=TaskStatus.TO_DO  
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        todo_queue.enqueue(new_task)

        task_map.put(new_task, 'To Do') 

        return new_task


@router.get("/{project_id}/tasks/todo", response_model=List[TaskResponse])
async def get_todo_tasks(project_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(
        and_(Task.project_id == project_id, Task.status == TaskStatus.TO_DO)
    ).all()
    for task in tasks:
        todo_queue.enqueue(task)
        task_map.put(task, 'To Do') 
    return [todo_queue.dequeue() for _ in range(len(todo_queue))]


@router.get("/{project_id}/tasks/doing", response_model=List[TaskResponse])
async def get_doing_tasks(project_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(
        and_(Task.project_id == project_id, Task.status == "doing")
    ).all()
    for task in tasks:
        doing_queue.enqueue(task)
        task_map.put(task, 'Doing') 
    return [doing_queue.dequeue() for _ in range(len(doing_queue))]


@router.get("/{project_id}/tasks/done", response_model=List[TaskResponse])
async def get_done_tasks(project_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(
        and_(Task.project_id == project_id, Task.status == "done")
    ).all()
    for task in tasks:
        done_queue.enqueue(task)
        task_map.put(task, 'Done')
    return [done_queue.dequeue() for _ in range(len(done_queue))]


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
            detail="You are not allowed to update this task"
        )

    if db_task.status != task.status:
        if db_task.status == "to do":
            todo_queue.dequeue()
        elif db_task.status == "doing":
            doing_queue.dequeue()
        elif db_task.status == "done":
            done_queue.dequeue()

        if task.status == "to do":
            todo_queue.enqueue(db_task)
        elif task.status == "doing":
            doing_queue.enqueue(db_task)
        elif task.status == "done":
            done_queue.enqueue(db_task)

        task_map.remove(db_task) 
        task_map.put(db_task, task.status) 

    db_task.name = task.name
    db_task.description = task.description
    db_task.start_date = task.start_date
    db_task.end_date = task.end_date
    db_task.employee_id = task.employee_id
    db_task.status = task.status

    db.commit()
    db.refresh(db_task)
    return db_task
