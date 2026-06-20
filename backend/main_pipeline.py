import easyocr
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
def clean_text(text):
    text = text.lower()
    text = " ".join(text.split())
    return text

reader = easyocr.Reader(['en'])

result = reader.readtext('dataset/payments/p1.png')

raw_text = ""

for item in result:
    raw_text += item[1] + " "

cleaned_text = clean_text(raw_text)
embedding = model.encode(cleaned_text)
print("Raw OCR Text:")
print(raw_text)

print("\nCleaned Text:")
print(cleaned_text)

print("\nEmbedding Length:")
print(len(embedding))
print("\nSearch Ready: True")