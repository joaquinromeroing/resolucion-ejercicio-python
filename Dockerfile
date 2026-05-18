FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install pytest pytest-mock pandas

CMD ["pytest", "tests/test_unificado.py"]