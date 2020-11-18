FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app/

# Install dependencies
COPY app/requirements.txt /app
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -U -r requirements.txt


COPY app/app /app
ENV PYTHONPATH=/app