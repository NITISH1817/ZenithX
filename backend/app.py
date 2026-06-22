
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SnapMind AI backend running"}

@app.get("/search")
def search():
    return {"query": "amazon payment", "result": "p1.png"}

screenshots = [
    "transaction successful amazon pay",
    "irctc train ticket chennai",
    "python index error list out of range",
    "amazon order delivered"
]