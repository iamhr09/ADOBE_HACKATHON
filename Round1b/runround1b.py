# run_round1b.py

import os
import json
import time
from datetime import datetime

from summarizer import summarize_documents
from ranker import rank_sections
from shared.document_parser import load_pdf_texts
from shared.utils import load_json

INPUT_DIR = "/app/data/input"
OUTPUT_DIR = "/app/output"
PERSONA_FILE = "/app/data/persona.json"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("🔍 Loading persona...")
    persona_data = load_json(PERSONA_FILE)
    persona = persona_data.get("persona")
    job = persona_data.get("job_to_be_done")

    print("📂 Reading input PDFs...")
    pdf_data = load_pdf_texts(INPUT_DIR)

    print("🧠 Extracting summaries + ranks...")
    summaries = summarize_documents(pdf_data, persona, job)
    ranked_sections = rank_sections(summaries)

    print("📝 Preparing final output...")
    output = {
        "metadata": {
            "persona": persona,
            "job_to_be_done": job,
            "documents": list(pdf_data.keys()),
            "timestamp": datetime.utcnow().isoformat()
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for i, item in enumerate(ranked_sections, start=1):
        output["extracted_sections"].append({
            "document": item["document"],
            "page_number": item["page"],
            "section_title": item["section_title"],
            "importance_rank": i
        })

        output["subsection_analysis"].append({
            "document": item["document"],
            "page_number": item["page"],
            "refined_text": item["refined_summary"],
            "importance_rank": i
        })

    print("💾 Saving output to /app/output/output.json")
    with open(os.path.join(OUTPUT_DIR, "output.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("✅ Done.")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"⏱️ Total runtime: {round(time.time() - start, 2)} seconds")
