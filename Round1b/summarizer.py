from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def chunk_text(text, max_tokens=500):
    sentences = text.split('. ')
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(tokenizer.tokenize(current_chunk + sentence)) < max_tokens:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_with_local_model(text, max_length=120, outline=None):
    if outline:
        print("🔍 Using structure to assist summarization...")

    chunks = chunk_text(text)
    summaries = []
    for idx, chunk in enumerate(chunks):
        prefix = ""
        if outline:
            
            matching_heading = next((h["text"] for h in outline["headings"] if h["page"] == idx + 1), "")
            prefix = f"Context: {matching_heading}\n"

        input_text = prefix + "summarize: " + chunk
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
        summary_ids = model.generate(inputs["input_ids"], max_length=max_length, num_beams=4, early_stopping=True)
        summaries.append(tokenizer.decode(summary_ids[0], skip_special_tokens=True))

    return " ".join(summaries)

