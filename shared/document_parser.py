import fitz  # PyMuPDF
import os

def extract_text_by_page(pdf_path, min_length=50):
    """
    Extracts page-wise text from a PDF.
    Filters out pages with text shorter than min_length.
    Returns: list of (page_number, text)
    """
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"❌ Error opening {pdf_path}: {e}")
        return []

    page_texts = []

    for page_num in range(len(doc)):
        try:
            page = doc.load_page(page_num)
            text = page.get_text().strip()
            if len(text) >= min_length:
                page_texts.append((page_num + 1, text))
        except Exception as e:
            print(f"⚠️ Error reading page {page_num+1} of {pdf_path}: {e}")

    return page_texts

def extract_documents(input_dir):
    docs = {}
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(input_dir, filename)
            doc = fitz.open(path)
            pages = []
            for i, page in enumerate(doc):
                text = page.get_text()
                pages.append((i + 1, text))
            docs[filename] = pages
    return docs