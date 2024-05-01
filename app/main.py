from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel, Field, create_engine , select
from sqlmodel import Session
from contextlib import asynccontextmanager


from app import settings

# Step 1: Database Table SCHEMA

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    
connection_string: str = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
engine = create_engine(connection_string)


def create_db_tables(): 
    print("Create_db_tables")
    SQLModel.metadata.create_all(engine)
    print("done")
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Startup")
    create_db_tables()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/db")
def db_var():
    return("DB",settings.DATABASE_URL, "Connection",  connection_string)

@app.post("/todo")
def create_todo(todo_data: Todo):
        with Session(engine) as session:
            session.add(todo_data)
            session.commit()
            session.refresh(todo_data)
            return todo_data

# Get all todos

@app.get("/todo")
def get_all_todos():
    with Session(engine) as session:
        query = select(Todo)
        all_todos = session.exec(query).all()
        return all_todos