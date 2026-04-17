# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Instalamos pandas (lo necesario para correr el script)
RUN pip install pandas

# Definimos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de la app y los datos a /app según la consigna
COPY app/analisis.py /app/
COPY data/datos.csv /app/

# Comando por defecto al levantar el contenedor
CMD ["python", "analisis.py"]
