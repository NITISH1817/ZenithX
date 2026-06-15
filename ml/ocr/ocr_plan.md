# OCR Module Plan

## Goal

Extract text from uploaded screenshots so that the AI system can understand the information inside images.

---

## Input

Screenshot image

Examples:

- Payment screenshot
- Ticket screenshot
- Coding error screenshot
- Notes screenshot

---

## Output

Extracted text from image

Example:

Input:
Google Pay screenshot

Output:

Transaction Successful
Amount 500
Receiver Amazon Pay

---

## Planned Library

EasyOCR (Python)

---

## Process Pipeline

1. User uploads screenshot

2. OCR reads image

3. Extract visible text

4. Save extracted text

5. Send extracted text for semantic search

---

## Future Implementation

Python Example

```python
import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext('image.png')
```

---

## Expected Role In Project

OCR is the first stage of intelligence because it converts screenshots into readable information.
