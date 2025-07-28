FROM python:3.10-slim

WORKDIR /app
ENV PYTHONIOENCODING=UTF-8


COPY Round1b/ ./
COPY shared/ ./shared

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "runround1b.py"]
