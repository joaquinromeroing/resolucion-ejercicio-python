FROM python:3.9-slim
RUN pip install --no-cache-dir pandas
RUN mkdir /data
COPY data/datos.csv /data/datos.csv
WORKDIR /app
COPY app/analisis.py .
CMD ["python", "analisis.py"]
