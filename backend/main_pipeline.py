import os
import json
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

DATASET_PATH = "dataset"

folders = [
    "payments",
    "coding",
    "notes",
    "shopping",
    "travel"
]


def clean_text(text):
    text = text.lower()

    # Common OCR fixes
    text = text.replace("₹", "")
    text = text.replace("?", "")
    text = text.replace("|", "1")

    # Fix 50o -> 500
    text = re.sub(r'(?<=\d)o(?=\d)', '0', text)

    text = " ".join(text.split())

    return text

ocr_data = {}

for folder in folders:

    folder_path = os.path.join(DATASET_PATH, folder)

    for filename in os.listdir(folder_path):

        if filename.endswith(".png"):

            image_path = os.path.join(folder_path, filename)

            print("Processing:", image_path)

            result = reader.readtext(
                image_path,
                detail=0,
                paragraph=True
            )

            text = clean_text(" ".join(result))

            ocr_data[f"{folder}/{filename}"] = text

with open("dataset/ocr_output.json", "w", encoding="utf-8") as f:
    json.dump(ocr_data, f, indent=4)

print("Done")
print("Images:", len(ocr_data))