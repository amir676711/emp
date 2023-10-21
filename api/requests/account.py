from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union
from uuid import UUID


class CreateUserRequest(BaseModel):
    FName:str
    LName:str
    EmpCode:int
    RoleID:int
    isAdmin:bool
    Password:str
    Tell:str

class EditUserRequest(BaseModel):
    ID:UUID
    FName:str
    LName:str
    EmpCode:int
    RoleID:int
    isAdmin:bool
    Tell:str
class LoginRequest(BaseModel):
    EmpCode:int
    Password:str

class UserPasswordChangeRequest(BaseModel):
    EmpCode:int
    Password:str