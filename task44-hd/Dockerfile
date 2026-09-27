FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app.py .

RUN useradd -m appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /app /data

USER appuser

ENTRYPOINT ["python", "app.py"]