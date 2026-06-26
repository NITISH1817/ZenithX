import json
import numpy as np

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# -----------------------------
# Enable CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Serve Images
# -----------------------------
app.mount("/dataset", StaticFiles(directory="dataset"), name="dataset")

# -----------------------------
# Load Model
# -----------------------------
print("Loading Sentence Transformer...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Load OCR Data
# -----------------------------
with open("dataset/ocr_output.json", "r", encoding="utf-8") as f:
    ocr_data = json.load(f)

screenshots = []

for image_path, text in ocr_data.items():
    screenshots.append({
        "image": image_path,
        "text": text.lower()
    })

texts = [item["text"] for item in screenshots]

print("Generating embeddings...")
embeddings = model.encode(texts)

print(f"Loaded {len(screenshots)} screenshots")

# -----------------------------
# Search Function
# -----------------------------
def semantic_search(query, threshold=0.40):

    query = query.lower().strip()

    # Exact keyword search
    for item in screenshots:
        if query in item["text"]:
            print("Exact Match Found")
            return (
                item["image"],
                item["text"],
                1.0
            )

    # Semantic Search
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)

    best_index = np.argmax(scores)
    best_score = float(scores[0][best_index])

    print("\n========== DEBUG ==========")
    print("Query :", query)
    print("Best Image :", screenshots[best_index]["image"])
    print("Score :", best_score)
    print("===========================\n")

    if best_score < threshold:
        return None

    return (
        screenshots[best_index]["image"],
        screenshots[best_index]["text"],
        best_score
    )

# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "SnapMind AI Backend Running"
    }

# -----------------------------
# Search API
# -----------------------------
@app.get("/search")
def search(query: str):

    result = semantic_search(query)

    if result is None:
        return {
            "found": False,
            "message": "No matching screenshot found."
        }

    image, text, score = result

    return {
        "found": True,
        "query": query,
        "image": image,
        "text": text,
        "score": round(score, 3)
    }