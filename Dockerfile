FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# HuggingFace Spaces open port 7860 by default for Docker instances
EXPOSE 7860

CMD ["gunicorn", "-b", "0.0.0.0:7860", "-t", "120", "app:app"]
