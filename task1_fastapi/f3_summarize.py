# f3_summarize.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/summarize")
def summarize(data: TextData):
    word_count = len(data.text.split())
    return {"word_count": word_count}
