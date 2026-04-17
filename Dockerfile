FROM python:3.11-slim

WORKDIR /app

RUN pip install pandas

COPY app/ /app/
COPY data/ /data/

CMD ["python", "analisis.py"]
