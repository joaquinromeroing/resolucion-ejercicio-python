FROM python:3.12-slim

WORKDIR /proyecto

COPY app/ ./app/
COPY data/ ./data/

RUN pip install --no-cache-dir pandas
RUN mkdir -p /proyecto/output

CMD ["python", "app/analisis.py"]