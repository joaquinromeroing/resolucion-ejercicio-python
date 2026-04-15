# Usa Python 3.9
FROM python:3.9-slim

# Instala Pandas (Requisito punto 4)
RUN pip install pandas

# Define donde va a vivir el código
WORKDIR /app

# Copia el script
COPY ./app/analisis.py .

# Ejecuta el script
CMD ["python", "analisis.py"]