FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas

COPY app/ /app/app/
COPY data/ /app/data/

RUN mkdir -p /app/output

CMD ["python", "/app/app/analisis.py"]
