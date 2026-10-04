import time
from fastapi  import FastAPI
from fastapi.params  import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, votes
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


