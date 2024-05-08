from fastapi import FastAPI
from sqlmodel import SQLModel, Field


# Create Model

class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title : str = Field()
    description : str = Field()
    is_completed : bool = Field()



@app.get("/")
async def root():
    return {"Message": "Welcome to dailyDo todo App"}