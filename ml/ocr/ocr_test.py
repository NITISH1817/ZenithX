import easyocr
import json

reader = easyocr.Reader(['en'])

result = reader.readtext('dataset/payments/p1.png')

text = " ".join([item[1] for item in result])

data = {
    "p1.png": text
}

with open("dataset/ocr_output.json", "w") as file:
    json.dump(data, file, indent=4)

print("OCR output saved successfully")