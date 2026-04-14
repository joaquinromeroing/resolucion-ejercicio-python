FROM python:3.11-slim

RUN pip install --no-cache-dir pandas

RUN mkdir /data /output /app

COPY app/analisis.py /app/analisis.py

WORKDIR /app

CMD ["python", "analisis.py"]
