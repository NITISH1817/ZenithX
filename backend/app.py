from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample screenshot database
screenshots = [
    "transaction successful amazon pay",
    "irctc train ticket chennai",
    "python index error list out of range",
    "amazon order delivered",
    "college operating systems notes"
]

# Generate embeddings once at startup
embeddings = model.encode(screenshots)


def semantic_search(query):
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)

    best_match = np.argmax(scores)

    return (
        screenshots[best_match],
        float(scores[0][best_match])
    )


@app.get("/")
def home():
    return {"message": "SnapMind AI backend running"}


@app.get("/search")
def search(query: str):
    result, score = semantic_search(query)

    return {
        "query": query,
        "result": result,
        "score": round(score, 3)
    }