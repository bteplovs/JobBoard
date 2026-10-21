from fastapi import Depends, FastAPI

from database import create_db_and_tables

from .dependencies import get_query_token
from .routers import users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
