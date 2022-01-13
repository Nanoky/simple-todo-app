from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/tasks")
def getAll():
    return {'message' : "Hello world"}


