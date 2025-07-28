def load_persona_and_job(persona_path, job_path):
    with open(persona_path, "r", encoding="utf-8") as f:
        persona = f.read().strip()

    with open(job_path, "r", encoding="utf-8") as f:
        job = f.read().strip()

    return persona, job


def build_prompt(persona, job_to_do, page_text, document_name, page_number):
    prompt = f"""
You are a helpful assistant for the persona below:

📌 Persona: {persona}
🎯 Task: {job_to_do}

You are reading **Page {page_number}** of the document: "{document_name}"

Based on the page content below, extract the most relevant insight that helps the persona achieve their task.

Respond in this format:
Summary: <your summary here, 3–5 lines>
Importance: <1–5>
Section Title (if any): <Optional title>

[Page Content Starts]
{page_text}
[Page Content Ends]
""".strip()

    return prompt
