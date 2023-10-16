from fastapi import FastAPI
from api.handlers import account


from sqlalchemy.orm import Session

from database import CRUD, models
from database.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

def create_app():
    app = FastAPI()
    app.include_router(router=account.router)
    
    return app