import json
import re
import numpy as np

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------- Static Images -------------

app.mount("/dataset", StaticFiles(directory="dataset"), name="dataset")

# ------------ Load Model ------------

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------ Load OCR ------------

with open("dataset/ocr_output.json", "r", encoding="utf-8") as f:
    ocr_data = json.load(f)

screenshots = []

for image, text in ocr_data.items():
    screenshots.append({
        "image": image,
        "text": text.lower()
    })

texts = [x["text"] for x in screenshots]
embeddings = model.encode(texts)

print("Loaded", len(screenshots), "screenshots")


# ------------ Search ------------

def semantic_search(query, threshold=0.45):

    query = query.lower().strip()

    # ---------- Exact Match ----------
    for item in screenshots:
        if query in item["text"]:
            print("Exact Match")
            return (
                item["image"],
                item["text"],
                1.0
            )

    # ---------- Token Match ----------
    words = re.findall(r"\w+", query)

    best_keyword = None
    best_count = 0

    for item in screenshots:

        count = 0

        for word in words:
            if word in item["text"]:
                count += 1

        if count > best_count:
            best_count = count
            best_keyword = item

    if best_keyword is not None and best_count > 0:

        score = best_count / len(words)

        return (
            best_keyword["image"],
            best_keyword["text"],
            score
        )

    # ---------- Semantic Search ----------

    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)

    best_index = np.argmax(scores)

    best_score = float(scores[0][best_index])

    print("\n==============================")
    print("Query :", query)
    print("Best Image :", screenshots[best_index]["image"])
    print("Score :", best_score)
    print("==============================\n")

    if best_score < threshold:
        return None

    return (
        screenshots[best_index]["image"],
        screenshots[best_index]["text"],
        best_score
    )


# ------------ Routes ------------

@app.get("/")
def home():
    return {
        "message": "SnapMind AI Backend Running"
    }


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