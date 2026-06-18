from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

text1 = "upi payment receipt"
text2 = "upi transaction payment successful"

emb1 = model.encode([text1])
emb2 = model.encode([text2])

score = cosine_similarity(emb1, emb2)

print(score)