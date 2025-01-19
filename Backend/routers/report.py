import pandas as pd
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from Backend.models import Project, User
from Backend.auth.auth_handler import get_db, get_current_active_user
from io import BytesIO
from fastapi.responses import StreamingResponse
from datetime import datetime
from sqlalchemy import or_
import openpyxl

router = APIRouter()

@router.get("/projects/export")
async def export_projects(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_active_user)
):
    projects = db.query(Project).filter(
        or_(
            Project.owner_id == current_user.id,
            Project.employees.any(id=current_user.id)
        )
    ).all()

    project_data = [
        {
            "Project Name": project.title,
            "Start Date": project.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "End Date": project.end_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Status": "Ongoing" if project.end_date > datetime.utcnow() else "Completed"
        }
        for project in projects
    ]

    df = pd.DataFrame(project_data)

    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Projects")
    
    excel_file.seek(0)

    return StreamingResponse(excel_file, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=projects.xlsx"})
