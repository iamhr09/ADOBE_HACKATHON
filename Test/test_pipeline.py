import os
import json
import shutil
from main import main  # assuming main.py has a callable main()

# Setup test environment
TEST_INPUT_DIR = "input"
TEST_OUTPUT_DIR = "output"
TEST_PERSONA_FILE = os.path.join(TEST_INPUT_DIR, "persona.txt")
TEST_JOB_FILE = os.path.join(TEST_INPUT_DIR, "job.txt")
TEST_OUTPUT_FILE = os.path.join(TEST_OUTPUT_DIR, "output.json")

def setup_test_files():
    os.makedirs(TEST_INPUT_DIR, exist_ok=True)
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

    # Write sample persona
    with open(TEST_PERSONA_FILE, "w") as f:
        f.write("Investment Analyst")

    # Write sample job
    with open(TEST_JOB_FILE, "w") as f:
        f.write("Analyze R&D spending")

    # Copy sample PDFs to input folder
    # Assuming you have some sample PDFs in ./sample_pdfs/
    sample_pdf_dir = "sample_pdfs"
    if os.path.exists(sample_pdf_dir):
        for pdf in os.listdir(sample_pdf_dir):
            if pdf.lower().endswith(".pdf"):
                shutil.copy(os.path.join(sample_pdf_dir, pdf), TEST_INPUT_DIR)
    else:
        print("⚠️ sample_pdfs folder not found. Please add test PDFs.")

def validate_output():
    if not os.path.exists(TEST_OUTPUT_FILE):
        print("❌ Output file not generated.")
        return False

    with open(TEST_OUTPUT_FILE, "r") as f:
        data = json.load(f)

    # Basic validations
    if "persona" not in data or "job" not in data or "documents" not in data:
        print("❌ Output JSON missing required keys.")
        return False

    if not isinstance(data["documents"], dict) or len(data["documents"]) == 0:
        print("❌ No documents found in output JSON.")
        return False

    # Check at least one document has sections
    has_sections = False
    for doc, sections in data["documents"].items():
        if isinstance(sections, list) and len(sections) > 0:
            has_sections = True
            # Check required keys in first section
            keys = ["page_number", "summary", "importance", "section_title"]
            if not all(k in sections[0] for k in keys):
                print(f"❌ Missing keys in sections of document {doc}.")
                return False
    if not has_sections:
        print("❌ No sections found in any document.")
        return False

    print("✅ Output JSON structure looks good.")
    return True

def clean_test_environment():
    # Optional: clear input and output folders before next run
    shutil.rmtree(TEST_INPUT_DIR, ignore_errors=True)
    shutil.rmtree(TEST_OUTPUT_DIR, ignore_errors=True)

def run_test():
    print("🔧 Setting up test files...")
    setup_test_files()

    print("▶️ Running main pipeline...")
    main()

    print("🔍 Validating output...")
    success = validate_output()

    if success:
        print("🎉 Test passed!")
    else:
        print("❌ Test failed.")

if __name__ == "__main__":
    run_test()
