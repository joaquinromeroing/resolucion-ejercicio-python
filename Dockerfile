FROM python:3.11

RUN pip install pandas

RUN mkdir -p /app /data /output

COPY app/analisis.py /app/analisis.py

WORKDIR /app

CMD ["python", "analisis.py"]