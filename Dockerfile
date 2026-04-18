FROM python:3.11

WORKDIR /app

RUN pip install pandas

COPY data ./data
COPY app ./app

RUN mkdir output

CMD ["python3", "app/analisis.py"]

