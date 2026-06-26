Yes. Since your project has evolved beyond the initial idea, your README should reflect the actual implementation rather than the original plan. Here's a polished version you can use.

📸 SnapMind AI
Search Memories, Not Filenames

SnapMind AI is an AI-powered semantic screenshot search engine that enables users to retrieve screenshots using natural language. Instead of searching by filename or date, SnapMind AI understands the content inside screenshots using OCR and semantic similarity.

👥 Team Members
Nitish Priyan R S

Ragavarthini R

Kavya N

📖 Problem Statement
Modern smartphone users store hundreds or even thousands of screenshots containing valuable information such as:

Payment receipts

Train and flight tickets

Coding errors

Class notes

Shopping orders

Booking confirmations

Traditional gallery applications organize screenshots only by date or filename, making it difficult to retrieve important information later. Users often spend several minutes scrolling through screenshots to locate a single image.

This creates a digital memory retrieval problem.

💡 Our Solution
SnapMind AI uses Artificial Intelligence to understand the meaning of screenshots instead of relying on filenames.

Users can search naturally using queries like:

Find my UPI payment screenshot

Show my Python error screenshot

Find train ticket

Show shopping receipt

The system returns the most relevant screenshot along with its similarity score.

✨ Features
OCR-based text extraction

AI-powered semantic search

Natural language queries

Screenshot preview

Similarity score

Responsive modern UI

FastAPI REST API

Dynamic search counter

Theme switching

Smooth animations

🛠 Tech Stack
Frontend
HTML5

CSS3

JavaScript

Backend
FastAPI

Python

AI / Machine Learning
EasyOCR

Sentence Transformers (all-MiniLM-L6-v2)

Scikit-learn

NumPy

🏗 Project Architecture
Screenshots
      │
      ▼
EasyOCR
(Text Extraction)
      │
      ▼
OCR Output (JSON)
      │
      ▼
Sentence Transformer
(Text Embeddings)
      │
      ▼
Cosine Similarity
      │
      ▼
FastAPI Backend
      │
      ▼
Frontend UI
📂 Project Structure
ZenithX
│
├── backend
│   ├── app.py
│   └── main_pipeline.py
│
├── dataset
│   ├── screenshots
│   └── ocr_output.json
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── favicon.ico
│
├── requirements.txt
└── README.md
🚀 Development Progress
Day 1
Repository setup

Project planning

MIT License

Day 2
Dataset collection

Screenshot categorization

Metadata preparation

Day 3
EasyOCR integration

OCR text extraction

Day 4
Text preprocessing

Normalization pipeline

Day 5
Sentence Transformer integration

Embedding generation

Day 6
Semantic retrieval

Cosine similarity search

Day 7
End-to-end AI pipeline

Day 8
FastAPI backend

Search API

Day 9
Dynamic semantic retrieval

Backend integration

Day 10
Natural language query support

Similarity score output

Day 11
Frontend development

Backend integration

UI enhancements

Day 12
Connected OCR dataset dynamically

Semantic search integration

Static image serving

CORS configuration

End-to-end testing

Search debugging and optimization

📊 Workflow
User enters a search query.

EasyOCR extracts text from screenshots.

Text is converted into embeddings using Sentence Transformers.

Cosine similarity compares the query with stored embeddings.

The most relevant screenshot is returned with its similarity score.

🔮 Future Improvements
Hybrid keyword + semantic search

CLIP image embeddings

Voice search

Mobile application

Cloud synchronization

Screenshot auto-categorization

Better OCR preprocessing

Multi-language support

🎯 Project Vision
Our vision is to transform screenshots into searchable knowledge by enabling users to retrieve important information using semantic understanding rather than manual scrolling.

SnapMind AI aims to make screenshot retrieval faster, smarter, and more intuitive with the power of Artificial Intelligence.

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/NITISH1817/ZenithX.git
2. Move into the project
cd ZenithX
3. Install dependencies
pip install -r requirements.txt
4. Start the backend
python3 -m uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
5. Open another terminal and start the frontend
cd frontend
python3 -m http.server 5501
6. Open in your browser
Frontend:

http://localhost:5501
Backend API:

http://localhost:8000
Swagger Documentation:

http://localhost:8000/docs
👨‍💻 Team ZenithX
SnapMind AI – Search Memories, Not Filenames.Yes. Since your project has evolved beyond the initial idea, your README should reflect the actual implementation rather than the original plan. Here's a polished version you can use.

📸 SnapMind AI
Search Memories, Not Filenames

SnapMind AI is an AI-powered semantic screenshot search engine that enables users to retrieve screenshots using natural language. Instead of searching by filename or date, SnapMind AI understands the content inside screenshots using OCR and semantic similarity.

👥 Team Members
Nitish Priyan R S

Ragavarthini R

Kavya N

📖 Problem Statement
Modern smartphone users store hundreds or even thousands of screenshots containing valuable information such as:

Payment receipts

Train and flight tickets

Coding errors

Class notes

Shopping orders

Booking confirmations

Traditional gallery applications organize screenshots only by date or filename, making it difficult to retrieve important information later. Users often spend several minutes scrolling through screenshots to locate a single image.

This creates a digital memory retrieval problem.

💡 Our Solution
SnapMind AI uses Artificial Intelligence to understand the meaning of screenshots instead of relying on filenames.

Users can search naturally using queries like:

Find my UPI payment screenshot

Show my Python error screenshot

Find train ticket

Show shopping receipt

The system returns the most relevant screenshot along with its similarity score.

✨ Features
OCR-based text extraction

AI-powered semantic search

Natural language queries

Screenshot preview

Similarity score

Responsive modern UI

FastAPI REST API

Dynamic search counter

Theme switching

Smooth animations

🛠 Tech Stack
Frontend
HTML5

CSS3

JavaScript

Backend
FastAPI

Python

AI / Machine Learning
EasyOCR

Sentence Transformers (all-MiniLM-L6-v2)

Scikit-learn

NumPy

🏗 Project Architecture
Screenshots
      │
      ▼
EasyOCR
(Text Extraction)
      │
      ▼
OCR Output (JSON)
      │
      ▼
Sentence Transformer
(Text Embeddings)
      │
      ▼
Cosine Similarity
      │
      ▼
FastAPI Backend
      │
      ▼
Frontend UI
📂 Project Structure
ZenithX
│
├── backend
│   ├── app.py
│   └── main_pipeline.py
│
├── dataset
│   ├── screenshots
│   └── ocr_output.json
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── favicon.ico
│
├── requirements.txt
└── README.md
🚀 Development Progress
Day 1
Repository setup

Project planning

MIT License

Day 2
Dataset collection

Screenshot categorization

Metadata preparation

Day 3
EasyOCR integration

OCR text extraction

Day 4
Text preprocessing

Normalization pipeline

Day 5
Sentence Transformer integration

Embedding generation

Day 6
Semantic retrieval

Cosine similarity search

Day 7
End-to-end AI pipeline

Day 8
FastAPI backend

Search API

Day 9
Dynamic semantic retrieval

Backend integration

Day 10
Natural language query support

Similarity score output

Day 11
Frontend development

Backend integration

UI enhancements

Day 12
Connected OCR dataset dynamically

Semantic search integration

Static image serving

CORS configuration

End-to-end testing

Search debugging and optimization

📊 Workflow
User enters a search query.

EasyOCR extracts text from screenshots.

Text is converted into embeddings using Sentence Transformers.

Cosine similarity compares the query with stored embeddings.

The most relevant screenshot is returned with its similarity score.

🔮 Future Improvements
Hybrid keyword + semantic search

CLIP image embeddings

Voice search

Mobile application

Cloud synchronization

Screenshot auto-categorization

Better OCR preprocessing

Multi-language support

🎯 Project Vision
Our vision is to transform screenshots into searchable knowledge by enabling users to retrieve important information using semantic understanding rather than manual scrolling.

SnapMind AI aims to make screenshot retrieval faster, smarter, and more intuitive with the power of Artificial Intelligence.

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/NITISH1817/ZenithX.git
2. Move into the project
cd ZenithX
3. Install dependencies
pip install -r requirements.txt
4. Start the backend
python3 -m uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
5. Open another terminal and start the frontend
cd frontend
python3 -m http.server 5501
6. Open in your browser
Frontend:

http://localhost:5501
Backend API:

http://localhost:8000
Swagger Documentation:

http://localhost:8000/docs
👨‍💻 Team ZenithX
SnapMind AI – Search Memories, Not Filenames.