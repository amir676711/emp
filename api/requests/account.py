from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union


class CreateUserRequest(BaseModel):
    FName:str
    LName:str
    EmpCode:int
    RoleID:int
    isAdmin:bool
    Password:str
    Tell:str