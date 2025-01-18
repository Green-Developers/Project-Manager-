from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Backend.routers import user, auth, project, task

app = FastAPI(debug=True)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(project.router, prefix="/projects", tags=["project"])
app.include_router(task.router, prefix="/Project", tags=["task"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
