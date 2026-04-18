FROM python:latest
WORKDIR /app
RUN pip install pandas
COPY app/ .
COPY data/ /data
CMD ["python", "analisis.py"] 
