FROM python:3.11
WORKDIR /app

RUN pip install pandas

COPY app/ /app/
COPY data/ /data/

CMD ["python", "analisis.py"]
