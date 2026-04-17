FROM python:3.11-slim

RUN pip install pandas

COPY data/ /data/
COPY app/ /app/

CMD ["python", "/app/analisis.py"]