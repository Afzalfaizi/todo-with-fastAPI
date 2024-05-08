from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session
from app import settings


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
session = Session(engine)

app: FastAPI = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Welcome to dailyDo todo App"}

@app.post("/todos")
async def create_todo():
    ...
    
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