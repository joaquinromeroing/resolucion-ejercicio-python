FROM python:3.9-slim

RUN pip install pandas

RUN mkdir /app /data /output

COPY app/analisis.py /app/analisis.py

CMD ["python", "/app/analisis.py"]