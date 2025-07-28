import fitz  
import unicodedata

def is_valid_heading(text):

    if len(text.strip()) < 2:
        return False

    if text.strip().isnumeric():
        return False

    non_symbol_chars = [c for c in text if unicodedata.category(c)[0] != "S"]
    if len(non_symbol_chars) < len(text) * 0.6:
        return False

    return True

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", "Untitled Document")
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    size = span["size"]
                    font = span.get("font", "")
                    flags = span.get("flags", 0)

                    
                    if not is_valid_heading(text):
                        continue

                    if size > 17:
                        level = "H1"
                    elif 14 < size <= 17:
                        level = "H2"
                    elif 12 < size <= 14:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num
                    })

    return {
        "title": title,
        "outline": outline
    }
