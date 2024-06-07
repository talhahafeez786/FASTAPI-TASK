from fastapi import APIRouter, Depends,  HTTPException, Request
from app.models import Task, User
from datetime import datetime
from typing import List

router = APIRouter()

tasks = {}

@router.post("/create-task")
def create_task(task : Task, request : Request):
    user = request.state.user
    if user not in tasks:
        tasks[user] = []
    task[user].append(task)
    return {"task_name" : task.task_name , "created_at" : task.created_at}

@router.get("/task", response_model = List[Task])
def get_task(request : Request):
    user = request.state.user
    if user in tasks:
        return tasks[user]
    else:
        raise HTTPException(status_code=401, detail="no task found")

@router.post("/template")
def template_form(request : Request):
    user = request.state.user
    return {"massege" : f"template form for {user}"}

@router.post("/login")
def login(credentials : User):
    if credentials.username == "user" and credentials.password == "password":
        return {"massege" : "Login Sucessfull"}
    else : 
        raise HTTPException(status_code=401, detail="Inavlid Credentials")
