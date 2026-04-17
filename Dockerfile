FROM python:3.11-slim

WORKDIR /app

RUN pip install pandas

COPY app/analisis.py /app/analisis.py

CMD ["python", "/app/analisis.py"]
