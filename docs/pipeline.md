# SnapMind AI Processing Pipeline

## Overview

SnapMind AI converts screenshots into searchable information using OCR and semantic search.

---

## Step 1: Screenshot Input

User uploads a screenshot.

Example:

- Payment screenshot
- Train ticket
- Coding error
- Notes screenshot

---

## Step 2: OCR Extraction

EasyOCR extracts text from the screenshot.

Example:

Input Screenshot:

Transaction Successful
Amazon Pay
₹500

Output Text:

Transaction Successful Amazon Pay ₹500

---

## Step 3: Text Preprocessing

The extracted text is cleaned.

Operations:

- Convert to lowercase
- Remove extra spaces

Example:

Input:

TRANSACTION SUCCESSFUL AMAZON PAY

Output:

transaction successful amazon pay

---

## Step 4: Embedding Generation

Sentence Transformer converts text into a semantic vector.

Example:

transaction successful amazon pay

↓

384-dimensional embedding

---

## Step 5: Semantic Retrieval

User enters a query.

Example:

amazon payment

The system compares the query embedding with screenshot embeddings and finds the most relevant screenshot.

---

## Final Workflow

Screenshot
↓
OCR
↓
Text Preprocessing
↓
Embedding Generation
↓
Semantic Search
↓
Relevant Screenshot Returned