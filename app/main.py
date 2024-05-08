from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, create_engine, Session
from app import settings
from typing import Annotated


# Create Model

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content : str = Field(min_length=3, max_length=60)
    is_completed : bool = Field(default=False)
    
    
# ENGINE IS ONE TIME IN WHOLE APPLICATION
connection_string : str = str (settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")
engine = create_engine(connection_string)

SQLModel.metadata.create_all(engine)



# Session: Separate session for each functionality/transaction
# session = Session(engine)

def get_session():
    with Session(engine) as session:
        yield session


app: FastAPI = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Welcome to dailyDo todo App"}

@app.post("/todos")
async def create_todo(todo:Todo, session:Annotated[Session,Depends(get_session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo
    
@app.get("/todos")
async def get_all_todos():
    ...

@app.get("/todos/{id}")
async def get_single_todo():
    ...
    
@app.put("/todos")
async def edit_todo():
    ...
    
@app.delete("/todos")
async def delete_todo():
    ...