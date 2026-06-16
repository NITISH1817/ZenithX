import easyocr
import json

reader = easyocr.Reader(['en'])

result = reader.readtext('dataset/payments/p1.png')

text = " ".join([item[1] for item in result])

print(text)