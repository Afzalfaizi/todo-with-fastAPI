from fastapi import FastAPI
from sqlmodel import SQLModel, Field,create_engine
from app import settings


# Create Model

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title : str = Field(min_length=3, max_length=15)
    description : str = Field(index=True, min_length=4, max_length=60)
    is_completed : bool = Field(default=False)
    
    
# ENGINE IS ONE TIME IN WHOLE APPLICATION
connection_string : str = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)


app: FastAPI = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Welcome to dailyDo todo App"}