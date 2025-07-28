# run_round1a.py

import os
import json
from structure_extractor import extract_outline  # Adjust path if needed

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Process all PDFs in input directory
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            print(f"📄 Processing: {filename}")

            try:
                result = extract_outline(pdf_path)  # Must return JSON-serializable dict
                output_filename = os.path.splitext(filename)[0] + ".json"
                output_path = os.path.join(OUTPUT_DIR, output_filename)

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                print(f"✅ Saved: {output_filename}")
            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    main()
