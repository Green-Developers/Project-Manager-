from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, Table, Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum


Base = declarative_base()

project_employees = Table(
    "project_employees",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    projects = relationship(
        "Project", secondary=project_employees, back_populates="employees", lazy="select"
    )
    tasks = relationship(
        "Task", back_populates="employee", cascade="all, delete", lazy="select"
    )


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(500), nullable=True)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="projects", lazy="joined")
    employees = relationship(
        "User", secondary=project_employees, back_populates="projects", lazy="select"
    )
    tasks = relationship(
        "Task", back_populates="project", cascade="all, delete", lazy="select"
    )


class TaskStatus(str, PyEnum):
    TO_DO = "TO_DO"
    DOING = "DOING"
    DONE = "DONE"


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)  
    employee_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.TO_DO) 

    project = relationship("Project", back_populates="tasks", lazy="joined")
    employee = relationship("User", back_populates="tasks", lazy="joined")
