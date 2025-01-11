from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from datastructures import LinkedList  # فرض می‌کنیم که این کلاس قبلاً تعریف شده

Base = declarative_base()

# مدل کاربر
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # ارتباط با پروژه‌ها
    projects = relationship("Project", secondary="project_employees", back_populates="employees")

# مدل پروژه
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, nullable=True, default=None)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))  # کلید خارجی

    # ارتباط با کاربر (مالک پروژه)
    owner = relationship("User", back_populates="projects")

    # لیست کارمندان از نوع LinkedList
    employees = None  # اینجا LinkedList ذخیره می‌شود

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employees = LinkedList()  # مقداردهی اولیه LinkedList
