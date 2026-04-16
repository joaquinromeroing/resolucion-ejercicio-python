FROM python:3.11
WORKDIR /app
RUN pip install pandas
COPY app/analisis.py .
COPY data/datos.csv /data/datos.csv
CMD ["python", "analisis.py"]
