from typing import List

from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from starlette.requests import Request
from starlette.responses import Response

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:  
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db
    

# Creating & Inserting Data
crud.create_table()


@app.get("/detect/{lat}&{lng}", response_model=schemas.StateCreate)
def read_user(lat: float, lng: float, db: Session = Depends(get_db)):
    db_user = crud.get_place(db, lat=lat, lng=lng)
    if db_user is None:
        raise HTTPException(status_code=404, detail="The location you inserted is out of the our database.")
    return db_user