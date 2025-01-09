from fastapi import FastAPI
from routers.users import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from db.engine import engine
from db import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router, prefix="/Users")
