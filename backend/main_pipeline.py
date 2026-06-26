import os
import json
import re
import easyocr

# ----------------------------
# Initialize OCR
# ----------------------------
reader = easyocr.Reader(['en'], gpu=False)

DATASET = "dataset"

folders = [
    "payments",
    "coding",
    "notes",
    "shopping",
    "travel"
]

output_file = os.path.join(DATASET, "ocr_output.json")

ocr_data = {}

# ----------------------------
# Clean OCR Text
# ----------------------------
def clean_text(text):
    text = text.lower()

    # Fix common OCR mistakes
    text = re.sub(r'(?<=\d)o(?=\d)', '0', text)
    text = re.sub(r'(?<=\d)l(?=\d)', '1', text)

    # Remove unwanted symbols
    text = re.sub(r'[^a-z0-9 ]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# ----------------------------
# OCR Processing
# ----------------------------
for folder in folders:

    folder_path = os.path.join(DATASET, folder)

    if not os.path.exists(folder_path):
        continue

    for file in os.listdir(folder_path):

        if not file.lower().endswith(".png"):
            continue

        image_path = os.path.join(folder_path, file)

        print(f"Processing: {image_path}")

        try:
            # Read text directly from image
            result = reader.readtext(image_path, detail=0)

            text = clean_text(" ".join(result))

            ocr_data[f"{folder}/{file}"] = text

            # Save after every image
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(ocr_data, f, indent=4)

        except Exception as e:
            print(f"Error processing {image_path}: {e}")

print("\nOCR Completed Successfully!")
print("Total Images Processed:", len(ocr_data))
print("Saved to:", output_file)