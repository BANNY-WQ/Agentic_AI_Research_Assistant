FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (if any models build wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source
COPY backend ./backend
COPY frontend ./frontend
COPY data ./data

# Expose the web port
EXPOSE 8000

# Start uvicorn serving both API and static frontend under single host
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]


