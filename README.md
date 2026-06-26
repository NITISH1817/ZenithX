# SnapMind AI

## Team Members
- Nitish Priyan R S
- Ragavarthini R
- Kavya N

## Problem Statement

Modern smartphone users store thousands of screenshots containing important information such as payment receipts, tickets, coding errors, notes, booking confirmations, and documents.

Current gallery applications organize screenshots only by date and filename, forcing users to manually scroll through hundreds of images when searching for important information.

This creates a digital memory retrieval problem.

## Our Solution

SnapMind AI is an AI-powered screenshot intelligence system that allows users to search screenshots using natural language.

Example searches:

- Find my UPI payment screenshot from April
- Show my Python error screenshot
- Find train ticket screenshot

Instead of searching by date, the system searches by meaning.

## Planned Features

- OCR Text Extraction
- Semantic Search
- Screenshot Categorization
- Natural Language Query Search
- Fast Retrieval Engine

## Proposed Tech Stack

Frontend:
- Next.js
- Tailwind CSS

Backend:
- FastAPI

AI/ML:
- EasyOCR
- Sentence Transformers
- FAISS Vector Search

Database:
- SQLite

## Repository Structure

(To be updated as project progresses)

## Progress Log

Day 1:
- Repository created
- MIT License added
- Initial project planning completed

More updates coming.
### Day 2

- Created dataset folders
- Collected screenshot samples for testing
- Organized screenshots into categories
- Added payment screenshots
- Added travel screenshots
- Added coding screenshots
- Added notes screenshots
- Added shopping screenshots
- Created metadata.csv for dataset mapping
- Planned OCR implementation pipeline

### Day 3 Completed

- Installed EasyOCR
- Extracted text from screenshots
- Tested OCR on dataset
- Documented OCR results
- Created OCR output structure

### Day 4 Completed

- Created text preprocessing module
- Implemented lowercase normalization
- Implemented whitespace cleanup
- Tested preprocessing on OCR output
- Documented preprocessing workflow

### Day 5 Completed

- Installed Sentence Transformers
- Generated semantic embeddings
- Tested similarity scoring
- Created embeddings documentation
- Began semantic search foundation

### Day 6 Completed

- Created semantic retrieval module
- Generated embeddings for screenshot corpus
- Implemented cosine similarity search
- Tested multiple natural language queries
- Documented retrieval results



### Day 7 Completed

- Created integrated processing pipeline
- Connected OCR with preprocessing module
- Connected preprocessing with embedding generation
- Built end-to-end screenshot processing workflow
- Tested complete pipeline using sample screenshots
- Documented system pipeline
  
### Day 8 Completed

- Created FastAPI backend service
- Built backend test endpoint
- Created search API endpoint
- Connected backend structure for retrieval system
- Documented API endpoints


### Day 9 Completed

- Connected backend API with semantic retrieval engine
- Implemented dynamic semantic search
- Removed hardcoded search response
- Tested multiple search queries
- Documented backend search testing

### Day 10 Completed

- Added dynamic search query input
- Tested multiple natural language searches
- Added similarity score output
- Improved search API usability
- Documented API usage

### Day 11 Completed

- Created frontend structure
- Built search interface
- Added UI styling
- Connected frontend with backend API
- Tested end-to-end search workflow
# Day 12 – Semantic Search Integration

## Overview

On Day 12, the focus was on integrating semantic search into SnapMind AI by connecting OCR-generated text with the FastAPI backend. The goal was to enable users to search screenshots using natural language queries instead of manually browsing through folders.

---

## Work Completed

- Integrated OCR output (`ocr_output.json`) into the backend.
- Loaded OCR text dynamically instead of using hardcoded screenshot data.
- Generated text embeddings using the `all-MiniLM-L6-v2` Sentence Transformer model.
- Implemented semantic search using cosine similarity.
- Added a similarity threshold to filter out irrelevant search results.
- Configured FastAPI to serve screenshot images using `StaticFiles`.
- Enabled CORS to allow communication between the frontend and backend.
- Connected the frontend search interface with the FastAPI search API.
- Added debugging logs to display the search query, best match, and similarity score.
- Tested search functionality across multiple screenshot categories such as Payments, Shopping, Coding, Notes, and Travel.

---

## Technologies Used

- Python
- FastAPI
- EasyOCR
- Sentence Transformers
- Scikit-learn
- NumPy
- HTML
- CSS
- JavaScript

---

## Files Updated

- `backend/app.py`
- `backend/main_pipeline.py`
- `frontend/script.js`
- `dataset/ocr_output.json`

---

## Outcome

- Successfully integrated semantic search with the OCR dataset.
- Enabled AI-based screenshot retrieval through a REST API.
- Improved backend architecture by dynamically loading OCR data.
- Identified OCR-related limitations and planned future improvements using hybrid keyword and semantic search.

---

## Future Improvements

- Improve OCR preprocessing for better text accuracy.
- Implement hybrid keyword and semantic search.
- Add image embeddings using CLIP.
- Enhance search accuracy for numeric queries.
 ---
- ## Project Vision

We are building an AI-powered system that helps users retrieve important information trapped inside screenshots by understanding semantic meaning instead of relying on manual scrolling.
