FROM python:3.13-slim

WORKDIR /app

COPY ./api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api/main.py .
COPY ./worker/worker.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
