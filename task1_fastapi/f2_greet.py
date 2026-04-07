# f2_greet.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}
