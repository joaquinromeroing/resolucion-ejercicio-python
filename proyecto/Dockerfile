FROM python:3.11

WORKDIR /app

COPY app/ /app/
COPY data/ /data/

RUN pip install pandas

CMD ["python", "analisis.py"]
