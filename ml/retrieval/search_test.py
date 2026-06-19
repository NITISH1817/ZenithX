from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

screenshots = [
    "transaction successful amazon pay",
    "irctc train ticket chennai",
    "python index error list out of range",
    "amazon order delivered",
    "college operating systems notes"
]

embeddings = model.encode(screenshots)

print("Total embeddings:", len(embeddings))