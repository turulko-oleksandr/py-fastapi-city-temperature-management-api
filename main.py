from fastapi import FastAPI
from config import get_db



app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
