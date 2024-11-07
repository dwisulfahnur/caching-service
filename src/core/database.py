from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from sqlmodel import SQLModel, create_engine
from src.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_dbsession():
    with Session(engine) as session:
        yield session

SQLModel.metadata.create_all(engine)

DBSessionDep = Annotated[Session, Depends(get_dbsession)]
