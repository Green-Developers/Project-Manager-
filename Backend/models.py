from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime
from enum import Enum as PyEnum


Base = declarative_base()

# جدول واسط بین پروژه‌ها و کاربران
project_employees = Table(
    "project_employees",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    projects = relationship("Project", secondary=project_employees, back_populates="employees")
    tasks = relationship("Task", back_populates="employee", cascade="all, delete")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="projects")
    employees = relationship("User", secondary=project_employees, back_populates="projects")
    tasks = relationship("Task", back_populates="project", cascade="all, delete")


class TaskStatus(PyEnum):
    TO_DO = "to do"
    DOING = "doing"
    DONE = "done"


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)  # ارتباط با پروژه
    employee_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # ارتباط با کارمند
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.TO_DO)  # وضعیت تسک

    project = relationship("Project", back_populates="tasks")
    employee = relationship("User", back_populates="tasks")