import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve dataset images
app.mount("/dataset", StaticFiles(directory="dataset"), name="dataset")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Screenshot database
screenshots = [
    {
        "text": "amazon payment successful",
        "image": "payments/p1.png"
    },
    {
        "text": "upi payment completed",
        "image": "payments/p2.png"
    },
    {
        "text": "google ads payment 500",
        "image": "payments/p3.png"
    },
    {
        "text": "amazon order delivered",
        "image": "payments/p4.png"
    },
    {
        "text": "payment receipt completed",
        "image": "payments/p5.png"
    },
    {
        "text": "python index error list out of range",
        "image": "coding/code1.png"
    },
    {
        "text": "python syntax error",
        "image": "coding/code2.png"
    },
    {
        "text": "operating systems notes",
        "image": "notes/n1.png"
    },
    {
        "text": "shopping cart amazon",
        "image": "shopping/shopping1.png"
    },
    {
        "text": "flight booking ticket",
        "image": "travel/t1.png"
    }
]

# Generate embeddings once
texts = [item["text"] for item in screenshots]
embeddings = model.encode(texts)


def semantic_search(query):
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)

    best_match = np.argmax(scores)

    return (
        screenshots[best_match]["image"],
        screenshots[best_match]["text"],
        float(scores[0][best_match])
    )


@app.get("/")
def home():
    return {
        "message": "SnapMind AI backend running"
    }


@app.get("/search")
def search(query: str):
    image, text, score = semantic_search(query)

    return {
        "query": query,
        "text": text,
        "image": image,
        "score": round(score, 3)
    }