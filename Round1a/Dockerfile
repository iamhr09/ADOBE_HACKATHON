FROM python:3.10-slim

WORKDIR /app

COPY Round1a/ ./
COPY shared/ ./shared

COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y && pip install --no-cache-dir -r requirements.txt && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "run_round1A.py"]
