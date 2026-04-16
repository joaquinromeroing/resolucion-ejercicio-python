FROM python:3.11

WORKDIR /app

COPY app/analisis.py /app/
COPY data/datos.csv /data/

RUN pip install pandas

CMD ["python", "analisis.py"]
