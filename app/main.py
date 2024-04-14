from fastapi import FastAPI
import uvicorn

from app import settings


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/db")
def db_var():
    return("DB", settings.DATABASE_URL)

