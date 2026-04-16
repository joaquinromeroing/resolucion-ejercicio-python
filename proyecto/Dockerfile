FROM python:3.11-slim

WORKDIR /app

RUN pip install pandas

COPY app/ /app/app/
COPY data/ /app/data/
COPY output/ /app/output/

CMD ["python", "app/analisis.py"]
