from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Backend.routers import user, auth, project, task, report

app = FastAPI(debug=True)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/user", tags=["Users"])
app.include_router(auth.router, prefix="/auth" , tags=["Authentication"])
app.include_router(project.router, prefix="/projects", tags=["Projects"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(report.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
