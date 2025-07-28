# output_formatter.py

import json
import time
from collections import defaultdict

def parse_groq_response(response_text):
    # Return the entire text as summary, dummy values for others
    return response_text, "N/A", "Untitled Section"



def build_output_json(persona, job, results_dict):
    """
    Build structured JSON from collected results
    results_dict = {
        "doc1.pdf": [
            {
                "page_number": 3,
                "summary": "...",
                "importance": 4,
                "section_title": "Revenue Growth"
            },
            ...
        ]
    }
    """
    extracted_sections = []
    sub_section_analysis = []

    for doc, entries in results_dict.items():
        # Sort by importance (descending)
        sorted_entries = sorted(entries, key=lambda x: x["importance"], reverse=True)

        # Add to extracted_sections
        for rank, entry in enumerate(sorted_entries, start=1):
            extracted_sections.append({
                "document": doc,
                "page_number": entry["page_number"],
                "section_title": entry["section_title"] or "Untitled Section",
                "importance_rank": rank
            })
            sub_section_analysis.append({
                "document": doc,
                "page_number": entry["page_number"],
                "refined_text": entry["summary"],
                "section_title": entry["section_title"] or "Untitled Section"
            })

    output = {
        "metadata": {
            "documents": list(results_dict.keys()),
            "persona": persona,
            "job": job,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis
    }

    return output


def save_output_json(output, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
