from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# مدل کاربر
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # ارتباط با پروژه‌ها
    projects = relationship("Project", back_populates="owner")

# مدل پروژه
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, nullable=True, default=None)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)  # زمان فعلی به‌صورت پیش‌فرض
    end_date = Column(DateTime, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))  # کلید خارجی

    # ارتباط با کاربر
    owner = relationship("User", back_populates="projects")


