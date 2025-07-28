# 🧠 Adobe Hackathon – Rounds 1A + 1B: Structured + Intelligent PDF Understanding

## 🚀 Overview

This project solves **Round 1A** and **Round 1B** of Adobe's *"Connecting the Dots"* Hackathon challenge.

It performs:

- **🔍 Round 1A:** Extracts structured document outlines (Title + Headings H1/H2/H3 with page numbers)
- **🧑‍🔬 Round 1B:** Summarizes pages based on persona & task (e.g., "Researcher" doing a "Literature Review")

All running **offline in Docker**, with multilingual support and no external APIs.

---

## 📂 What It Does

### ✅ Round 1A – Structure Extractor

- Extracts document `title`
- Detects H1/H2/H3 headings using font-size-based heuristics
- Supports multilingual text (Unicode compatible)
- Outputs structured `.json` outline

### ✅ Round 1B – Persona-Based Summarizer

- Accepts:
  - `persona.txt` (e.g., “I’m a Researcher”)
  - `job.txt` (e.g., “Do a literature review”)
- Summarizes each page as per the persona’s context
- Outputs final `.json` summaries, per document

---

## 📁 Project Structure

adobe-hackathon/
├── round1a/
│ ├── Dockerfile
│ ├── structure_extractor.py
│ └── output_formatter.py
│
├── round1b/
│ ├── summarizer.py
│ ├── document_parser.py
│ ├── main.py # Entry point for Rounds 1A + 1B
│ └── Dockerfile
│
├── shared/
│ └── utils.py
│
├── sample_data/
│ ├── input/
│ │ ├── persona.txt
│ │ ├── job.txt
│ │ └── test_pdfs/ # Drop your PDFs here
│ └── output/ # JSON output saved here
│
├── requirements.txt
├── .dockerignore
└── README.md


---

## 🐳 Docker Instructions

### 🔧 Build Docker Image (for linux/amd64)

```bash
docker build --platform=linux/amd64 -t adobe-hackathon -f round1b/Dockerfile .
```

 ## ▶️ Run Docker Container
On Linux/macOS

docker run --rm \
  -v "$(pwd)/sample_data/input:/app/input" \
  -v "$(pwd)/sample_data/output:/app/output" \
  adobe-hackathon


On Windows (CMD)

docker run --rm ^
  -v "%cd%\sample_data\input:/app/input" ^
  -v "%cd%\sample_data\output:/app/output" ^
  adobe-hackathon


## 📝 Input Requirements
sample_data/input/persona.txt → Persona (e.g., “I’m a Researcher”)

sample_data/input/job.txt → Task (e.g., “Do a literature review”)

sample_data/input/test_pdfs/ → Folder with .pdf files


## 📤 Output Format
All JSONs saved in sample_data/output/ with format:

Round 1A – Outline
```
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 }
  ]
}
```

Round 1B – Summarized Pages
```
{
  "document": "Understanding AI.pdf",
  "persona": "Researcher",
  "job": "Literature Review",
  "summaries": {
    "page_1": "This page introduces...",
    "page_2": "Key literature includes..."
  }
}
```

## 🧾 Dependencies
Declared in requirements.txt. Key packages:

PyMuPDF for PDF parsing

transformers, torch for summarization

sentencepiece, unicodedata


## ✅ Constraints Met

| Constraint      | ✅ Status                     |
| --------------- | ----------------------------   |
| CPU Only        | ✅ Yes                        |
| Fully Offline   | ✅ No API or network required |
| Multilingual    | ✅ Unicode supported          |
| < 10s PDF parse | ✅ Yes for ≤ 50 pages         |
| Persona Aware   | ✅ Summarizes per role/task   |


### ✨ Features
📖 Font-based structural outline extraction

🧠 Contextual summarization tailored to persona

📦 Dockerized, offline, and portable

🔣 Unicode + multilingual support

## 👨‍💻 Developed By
Quantum Coders – Adobe India Hackathon 2025
