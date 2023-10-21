from fastapi import APIRouter,Body,Depends,HTTPException
from entities import account
from api.responses.BaseMessage import BaseMessage
from api.responses.account import UserLoginResponse
from api.requests.account import CreateUserRequest,EditUserRequest,LoginRequest,UserPasswordChangeRequest
from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.CRUD import account
from uuid import UUID
import hashlib
import services.jwt as jwt


router = APIRouter(prefix="/api/v1/account")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/",status_code=201,response_model=BaseMessage)
def CreateNewUser(req : CreateUserRequest,db: Session = Depends(get_db)):
    newUser= account.create_user(db,req)
    if newUser is None :
        raise HTTPException(status_code=400,detail="Can Not Create User Account")
    return BaseMessage(message="User "+req.FName+" "+req.LName+ " created")

@router.get("/")
def GetAllUsers(db:Session=Depends(get_db)):
    return account.get_users(db)

@router.get("/{id}")
def GetUserDetail(id:UUID,db:Session=Depends(get_db) ):
    return account.get_user(db,id)

@router.patch("/",status_code=200,response_model=BaseMessage)
def EditUserDetail(req:EditUserRequest, db:Session=Depends(get_db)):
    user=account.get_user(db,req.ID)
    if user is None :
        raise HTTPException(status_code=404,detail="User Not Found")
    user.fName=req.FName
    user.lName=req.LName
    user.tell=req.Tell
    user.isAdmin=req.isAdmin
    user.empCode=req.EmpCode
    user.roleID=req.RoleID
    db.commit()
    return BaseMessage(message="user updated")


@router.patch("/changepass",status_code=200,response_model=BaseMessage)
def changepass(req:UserPasswordChangeRequest,db:Session=Depends(get_db)):
    user=account.get_user_by_emCode(db,req.EmpCode)
    if user is None :
        raise HTTPException(status_code=404 , detail="کاربر مورد نظر یافت نشد")
    hashed=hashlib.md5(req.Password.encode('utf-8'))
    user.password=hashed.hexdigest()
    db.commit()
    return BaseMessage(message="کلمه عبور کاربر با موفقیت تغییر کرد")    

@router.post("/login",status_code=200,response_model=UserLoginResponse)
def LoginUser(req:LoginRequest,db:Session=Depends(get_db)):
    user = account.login_user(db,req.EmpCode,req.Password)
    if user is None :
        raise HTTPException(status_code=404,detail="کاربر با مشخصات وارد شده یافت نشد")
    
    token=jwt.CreateToken({'id':str(user.id),'fname':user.fName,'lname':user.lName,'isAdmin':str(user.isAdmin),'role':str(user.roleID)})
    return UserLoginResponse(FullName=f"{user.fName} {user.lName}",EmpCode=user.empCode,RoleID=user.roleID,isAdmin=user.isAdmin,Token=token)
