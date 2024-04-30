from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel, Field, create_engine

from app import settings

# Step 1: Database Table SCHEMA

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    
connection_string: str = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)
# engine = create_engine(settings.DATABASE_URL)
    
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/db")
def db_var():
    return("DB",  settings.DATABASE_URL, "Connection",  connection_string)

