from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,UUID,DateTime
from sqlalchemy.orm import relationship
import uuid
from .database import Base
from .Types import BinaryUUID
class Account(Base):
    __tablename__ = "accounts"
    id = Column('id',BinaryUUID, primary_key=True, index=True,default=uuid.uuid4)
    fName = Column(String(300))
    lName = Column(String(300))
    empCode=Column(Integer,unique=True)
    roleID=Column(Integer)
    isAdmin = Column(Boolean, default=False)
    password = Column(String(300))
    tell=Column(String(15),unique=True)
    

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(600))

# class Report(Base):
#     __tablename__ = "reports"
#     id = Column(Integer,primary_key=True,index=True)
#     subject = Column(String)
#     text=Column(String)
#     CreatedDate: Column(DateTime)
#     creator:Column(UUID)
#     Receiver:Column(UUID)