from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

screenshots = [
    "transaction successful amazon pay",
    "irctc train ticket chennai",
    "python index error list out of range",
    "amazon order delivered",
    "college operating systems notes"
]

embeddings = model.encode(screenshots)

def semantic_search(query):
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)

    best_match = np.argmax(scores)

    return screenshots[best_match]

@app.get("/")
def home():
    return {"message": "SnapMind AI backend running"}

@app.get("/search")
def search():
    query = "amazon payment"

    result = semantic_search(query)

    return {
        "query": query,
        "result": result
    }