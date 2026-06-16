import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext('dataset/payments/p1.png')

print("\nExtracted Text:\n")

for item in result:
    print(item[1])