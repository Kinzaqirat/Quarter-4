# 📝 What are we building?
# We're building a simple API that lets you:

# Create and view users

# Create tasks for users

# Check or update tasks

from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4

from pydantic import BaseModel, EmailStr, constr

app = FastAPI()

# We're storing users and tasks in Python dictionaries for now:
user_db={}
task_db={}


class UserCreate(BaseModel):
    email: EmailStr
    username: constr(min_length=2, max_length=20)