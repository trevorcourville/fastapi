from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Create a new task 
@router.post("/")
def create_task(title: str, db: Session = Depends(get_db)):
    task = models.Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# List all tasks
@router.get("/")
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()