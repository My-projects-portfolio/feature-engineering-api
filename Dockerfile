# Use Python 3.11-slim image as the base
FROM python:3.11-slim

# Install necessary system dependencies for building pyarrow/fastparquet
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to avoid Python writing pyc files and to prevent cache during builds
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose port 8000 for FastAPI
ENV PORT=8000
EXPOSE 8000

# Run the application with uvicorn
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
