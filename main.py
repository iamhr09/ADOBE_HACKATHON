import os
import json
import fitz
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from Round1b.ranker import rank_chunks_tfidf  
from Round1b.prompt_builder import build_prompt  
from Round1a.structure_extractor import extract_outline  

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

MODEL_NAME = "google/flan-t5-small"

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_documents(folder_path):
    documents = {}
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(full_path)
            documents[filename] = {"text": text, "path": full_path}
        elif filename.lower().endswith(".txt"):
            with open(full_path, "r", encoding="utf-8") as f:
                documents[filename] = {"text": f.read(), "path": full_path}
    return documents

def chunk_text(text, max_tokens=400, tokenizer=None):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    current_len = 0
    for sent in sentences:
        sent_len = len(tokenizer.tokenize(sent)) if tokenizer else len(sent.split())
        if current_len + sent_len > max_tokens:
            chunks.append(current_chunk.strip())
            current_chunk = sent + " "
            current_len = sent_len
        else:
            current_chunk += sent + " "
            current_len += sent_len
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def summarize_text(text, persona, job, tokenizer, model, device, document_name="doc", chunk_id=1):
    prompt = build_prompt(persona, job, text, document_name, chunk_id)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
    outputs = model.generate(**inputs, max_length=150, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

def summarize_document(text, persona, job, tokenizer, model, device, document_name, structure=None):
    chunks = chunk_text(text, tokenizer=tokenizer)
    
    query = f"{persona} {job}"
    top_chunks = rank_chunks_tfidf(chunks, query, top_k=3)
    
    chunk_summaries = [
        summarize_text(chunk, persona, job, tokenizer, model, device, document_name, idx+1) 
        for idx, chunk in enumerate(top_chunks)
    ]
    combined_summary = " ".join(chunk_summaries)
    final_summary = summarize_text(combined_summary, persona, job, tokenizer, model, device, document_name, chunk_id="final")
    return final_summary

def get_user_inputs():
    persona = input("Enter persona (e.g., Researcher): ").strip()
    job = input("Enter job to be done (e.g., Literature review): ").strip()
    folder_path = input("Enter folder path containing docs: ").strip()
    use_structure = input("Use structure extraction (Round 1A)? (y/n): ").strip().lower().startswith("y")
    return persona, job, folder_path, use_structure

def main():
    persona, job, folder_path, use_structure = get_user_inputs()
    
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    
    documents = load_documents(folder_path)
    
    summaries = {}
    for fname, doc_info in documents.items():
        print(f"\n📄 Summarizing {fname} ...")
        structure_data = extract_outline(doc_info["path"]) if use_structure else None
        
        if use_structure:
            print("📑 Structure info extracted:")
            print("Title:", structure_data["title"])
            for h in structure_data["headings"]:
                print(f"{h['level']} - {h['text']} (Page {h['page']})")
        
        summary = summarize_document(
            doc_info["text"],
            persona,
            job,
            tokenizer,
            model,
            device,
            fname,
            structure=structure_data  
        )
        
        summaries[fname] = {
            "persona": persona,
            "job": job,
            "summary": summary,
            "used_structure": use_structure
        }
    
    output_file = "summaries.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=4)
    print(f"\n✅ All summaries saved to {output_file}")

if __name__ == "__main__":
    main()
