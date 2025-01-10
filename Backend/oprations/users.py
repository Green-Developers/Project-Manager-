from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from Backend.db.models import User


class Usersoprations:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    # متغیر user باید داخل متد create ساخته شود
    async def create(self, username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password=password)
        async with self.db_session as session:
            session.add(user)
            await session.commit()  # ذخیره کاربر در دیتابیس
        return user

    async def get_user_by_username(self, username: str) -> User:
        query = sa.select(User).where(User.username == username)
        async with self.db_session as session:
            result = await session.scalars(query)  # اصلاح برای دریافت داده‌ها
            
            user = result.first()  # گرفتن اولین نتیجه (در صورت وجود)
            if user is None:
                raise ValueError("User not found")
            return user
        
    async def login_user_by_username(self, username: str, 
                                     password: str) -> User:
        query = sa.select(User).where(
            sa.and_(User.username == username, User.password == password)
        )
        async with self.db_session as session:
            result = await session.scalars(query)
            user = result.first()
            if user is None:
                raise ValueError("User not found")
            return user