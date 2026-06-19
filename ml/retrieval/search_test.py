from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

screenshots = [
    "transaction successful amazon pay",
    "irctc train ticket chennai",
    "python index error list out of range",
    "amazon order delivered",
    "college operating systems notes"
]

embeddings = model.encode(screenshots)

query = "amazon payment"

query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding, embeddings)

best_match = np.argmax(scores)

print("Query:", query)
print("Best Match:", screenshots[best_match])