from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "transaction successful amazon pay"

embedding = model.encode(text)

print("Embedding Length:", len(embedding))