# 🔍 Adobe Hackathon – Round 1A: PDF Structure Extractor

## 📌 Challenge

Reimagine the PDF as an intelligent, interactive document. This module solves **Round 1A** of Adobe’s “Connecting the Dots” Hackathon by extracting a structured outline from a `.pdf` file.

It detects:
- 📖 Document title
- 🏷️ Headings: H1, H2, H3
- 📄 Corresponding page numbers

---

## ⚙️ What It Does

✅ Accepts `.pdf` files from `/app/input`  
✅ Extracts structured heading hierarchy based on font size  
✅ Supports multilingual text (e.g., Hindi, Japanese, Arabic)  
✅ Outputs `.json` files in `/app/output` following Adobe's format

### 🔢 Sample Output

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}


## **Project Structure**
adobe-hackathon-round1a/
├── round1a/
│   ├── Dockerfile
│   ├── run_round1a.py
│   ├── structure_extractor.py
│   └── output_formatter.py
├── shared/                  
│   └── utils.py  
|── Sample_data/
|    └── input/
|     |    └──sample_pdf/    <- drop your pdfs here
|     |── output/            <- processed JSON appear here 
|            
├── requirements.txt
├── .dockerignore
└── README.md                

## 🐳 **DOCKER INSTRUCTIONS**

🛠️ Build the Docker Image

docker build --platform=linux/amd64 -t adobe-round1a -f round1a/Dockerfile .

Run the Docker Container

for linux:-
docker run --rm \
  -v "$(pwd)/sample_data/input:/app/input" \
  -v "$(pwd)/sample_data/output:/app/output" \
  --network none \
  adobe-round1a

for Windows:-
  docker run --rm ^
  -v "%cd%\Sample_data\input\sample_pdf:/app/input" ^
  -v "%cd%\Sample_data\output:/app/output" ^
  adobe-round1a


📁 Make sure to place your .pdf files in sample_data/input/.
📝 The corresponding .json output will be generated in sample_data/output/.

## 🧾 Dependencies

All dependencies are listed in requirements.txt. Main ones include:

PyMuPDF==1.23.5
unicodedata  # (Python built-in)


## ✅ Constraints Met
| Constraint      | Status                          |
| --------------- | ------------------------------  |
| Execution Time  | ✅ Under 10s per 50-page PDF    |
| Model Size      | ✅ No ML model used             |
| CPU Only        | ✅ Yes                          |
| Offline Runtime | ✅ Fully offline (no API calls) |
| Architecture    | ✅ linux/amd64 compatible       |


## ✨ Features
🧠 Font-size–based heading hierarchy (H1/H2/H3)

🌐 Multilingual support with Unicode filtering

⚡ Fast and lightweight

📦 Dockerized for easy deployment and evaluation


## 🧑‍💻 Developed By
Quantum Coders
Adobe India Hackathon 2025 TEAM
📅 July 2025