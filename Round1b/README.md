# 🧠 Adobe Hackathon – Round 1B: Persona-Based Document Intelligence

## 📌 Challenge

Empower researchers to quickly navigate large PDFs by building **persona-aware intelligence**. This module solves **Round 1B** of Adobe’s “Connecting the Dots” Hackathon by generating **persona-aligned summaries** from PDF documents.

It focuses on:
- 👤 Understanding the reader's *persona* and *intent*
- 📄 Parsing the content of long academic PDFs
- 🧾 Summarizing based on contextually relevant goals (e.g., literature review, technical implementation)

---

## ⚙️ What It Does

✅ Accepts `.pdf` files from `/app/input`  
✅ Uses persona + job context to summarize key PDF content  
✅ Supports multi-page documents and text segmentation  
✅ Outputs persona-aligned `.json` summaries in `/app/output`  
✅ Runs **offline** using local FLAN-T5 model

---

### 🔢 Sample Output

```json
{
  "document": "AI_Research_Survey.pdf",
  "persona": "Researcher",
  "job": "Literature Review",
  "summary": [
    {
      "page": 1,
      "text": "This section provides an overview of classical machine learning techniques relevant to AI development..."
    },
    {
      "page": 2,
      "text": "The paper highlights supervised learning methods and compares SVMs with neural networks..."
    }
  ]
}


## **Project Structure**

ADOBE_PROJECT/
├── Round1b/
│   ├── Dockerfile
│   ├── runround1b.py
│   ├── prompt_builder.py
│   ├── ranker.py
│   ├── summarizer.py
├── shared/
│   ├── document_parser.py
│   └── utils.py
├── Sample_data/
│   ├── input/
│   │   └── sample_pdf/         <- Drop your PDFs here
│   └── output/                 <- Processed JSONs appear here
├── requirements.txt
└── README.md

## 🐳 **DOCKER INSTRUCTIONS**

🛠️ Build the Docker Image

docker build --platform=linux/amd64 -t adobe-round1b -f Round1b/Dockerfile .

🚀 Run the Docker Container

For Linux/macOS:
docker run --rm \
  -v "$(pwd)/Sample_data/input/sample_pdf:/app/input" \
  -v "$(pwd)/Sample_data/output:/app/output" \
  --network none \
  adobe-round1b

For Windows CMD/PowerShell:

docker run --rm ^
  -v "%cd%\Sample_data\input\sample_pdf:/app/input" ^
  -v "%cd%\Sample_data\output:/app/output" ^
  adobe-round1b


📁 Make sure to place your .pdf files in Sample_data/input/sample_pdf/.
📝 The corresponding .json summaries will appear in Sample_data/output/.


## 🧾 **Dependencies**
All dependencies are listed in requirements.txt. Main ones include:

transformers==4.41.1

torch

PyMuPDF==1.23.5

openai (used only if API support is extended — currently runs offline)

sentencepiece, scipy, tqdm, etc.


## ✅ **Constraints Met**

| Constraint      | Status                         |
| --------------- | ------------------------------ |
| Execution Time  | ✅ Under 15s per 50-page PDF    |
| Model Size      | ✅ FLAN-T5 Small (\~80MB)       |
| CPU Only        | ✅ Yes                          |
| Offline Runtime | ✅ Fully offline (no API calls) |
| Architecture    | ✅ linux/amd64 compatible       |


## ✨ **Features**
🧠 Persona-based prompt construction for relevance
📚 Supports large research documents
⚡ Local FLAN-T5 model for summarization
📦 Dockerized, offline, secure, and fast

## 🧑‍💻 **Developed By**
Quantum Coders
Adobe India Hackathon 2025 TEAM
📅 July 2025