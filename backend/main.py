from fastapi import FastAPI

from src.api import crud
from src.db.base import create_db


app = FastAPI()


create_db()
crud.crud(app)
