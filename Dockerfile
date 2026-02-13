FROM python:3.11-slim

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source + tests
COPY src ./src
COPY tests ./tests

# Ensure src is importable
ENV PYTHONPATH=/app/src

# Default: run tests
CMD ["pytest", "-q"]