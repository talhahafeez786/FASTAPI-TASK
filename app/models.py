from pydantic import BaseModel, Field
from datetime import datetime

class Task(BaseModel):
    task_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class User(BaseModel):
    username: str
    password: str
