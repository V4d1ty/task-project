FROM python:3.11-slim

WORKDIR /app
COPY task_app.py .
COPY tasks.json.example .

RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -m appuser && \
    mkdir -p /data && \
    chown -R appuser:appuser /app /data

USER appuser
EXPOSE 8001

HEALTHCHECK --interval=10s --timeout=3s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8001/health')" || exit 1

CMD ["python", "task_app.py", "serve"]