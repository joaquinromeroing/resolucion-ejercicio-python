FROM python:3.14

RUN pip install --upgrade pip setuptools wheel && \ 
    pip install pandas

# 2. Creamos las carpetas esperadas dentro del container 
RUN mkdir -p /data /output /app

# 3. Copiamos el CSV a la carpeta /data del contenedor
COPY data/datos.csv /data/datos.csv

# Copiamos el script a la carpeta /app del contenedor
COPY app/analysis.py /app/analysis.py

WORKDIR /app

CMD ["python", "analysis.py"]