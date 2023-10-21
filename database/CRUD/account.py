from uuid import UUID,uuid4
from sqlalchemy.orm import Session
import hashlib
from database import models
from entities.account import account
from entities.role import role
from api.requests.account import CreateUserRequest


def get_user(db: Session, user_id:UUID ):
    return db.query(models.Account).filter(models.Account.id == user_id).first()

def get_user_by_emCode(db: Session,empCode:int ):
    return db.query(models.Account).filter(models.Account.empCode == empCode).first()

def login_user(db: Session, empCode:int,password:str ):
    hashed_password = hashlib.md5(password.encode('utf-8'))
    print(hashed_password)
    return db.query(models.Account).filter(models.Account.empCode == empCode , models.Account.password== hashed_password.hexdigest()).first()


def create_user(db: Session, user: CreateUserRequest):
    hashed_password = hashlib.md5(user.Password.encode('utf-8'))
    generatedID=uuid4()
    db_user = models.Account(id=generatedID,fName=user.FName,lName=user.LName,empCode=user.EmpCode,roleID=user.RoleID,isAdmin=user.isAdmin,password=hashed_password.hexdigest(),tell=user.Tell)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:Session):
    return db.query(models.Account).all()