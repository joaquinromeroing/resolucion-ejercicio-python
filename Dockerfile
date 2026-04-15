FROM python:3.11

RUN pip install pandas

COPY app/ /app/
COPY data/ /data/

WORKDIR /app

CMD ["python", "analisis.py"]
