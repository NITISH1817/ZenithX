def clean_text(text):
    text = text.lower()
    text = " ".join(text.split())

    return text

ocr_text = """
Transaction Successful
Amazon Pay
500
ICICI Bank
"""

print("Original Text:")
print(ocr_text)

print("\nCleaned Text:")
print(clean_text(ocr_text))