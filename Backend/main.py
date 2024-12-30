from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import user,auth,projects

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

app.include_router(user.router, prefix="/user")
app.include_router(auth.router, prefix="/auth")
app.include_router(projects.router, prefix="/projects")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
