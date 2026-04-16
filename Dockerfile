FROM python:3.11

RUN pip install pandas

RUN mkdir /data /output /app

COPY app/analisis.py /app/analisis.py
COPY data/datos.csv /data/datos.csv

CMD ["python", "/app/analisis.py"]