FROM python:3.11-slim

RUN pip install pandas

COPY data/datos.csv /data/datos.csv
COPY app/analisis.py /app/analisis.py

CMD ["python", "/app/analisis.py"]