from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes import tasks, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Running"}