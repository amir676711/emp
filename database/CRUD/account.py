from uuid import UUID,uuid4
from sqlalchemy.orm import Session
import hashlib
from . import models
from entities.account import account
from entities.role import role
from api.requests.account import CreateUserRequest


def get_user(db: Session, user_id:UUID ):
    return db.query(models.account).filter(models.account.id == user_id).first()


def create_user(db: Session, user: CreateUserRequest):
    hashed_password = hashlib.md5(user.Password)
    generatedID=uuid4()
    db_user = models.account(id=generatedID,fName=user.FName,lName=user.LName,empCode=user.EmpCode,roleID=user.RoleID,isAdmin=user.isAdmin,password=hashed_password,tell=user.Tell)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user