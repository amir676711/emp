from fastapi import APIRouter,Body,Depends,HTTPException
from entities import account
from api.responses.BaseMessage import BaseMessage
from api.requests.account import CreateUserRequest
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database import CRUD
router = APIRouter(prefix="/api/v1/account")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewUser(req : CreateUserRequest,db: Session = Depends(get_db)):
    newUser= CRUD.account.create_user(db,req)
    if newUser is None :
        raise HTTPException(status_code=400,detail="Can Not Create User Account")
    return BaseMessage(message="User "+req.FName+" "+req.LName+ " created")

