from fastapi import FastAPI
from database import engine
from models import Base
from routers import todos_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}
