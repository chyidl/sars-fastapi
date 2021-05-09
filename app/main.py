from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import models, schemas
from .database import SessionLocal, engine

# create our models in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS or "Cross-Origin Resource Sharing" referes to the situations where a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a different "origin" than the frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    # ensures that any route passed this function ought to have our SessionLocal database connection when needed and that the session is closed after use.
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records
