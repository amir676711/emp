from pydantic import BaseModel

class UserLoginResponse (BaseModel):
    FullName:str
    EmpCode:int
    isAdmin:bool
    RoleID:int
    Token:str