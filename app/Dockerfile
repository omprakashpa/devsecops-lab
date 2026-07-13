# Intentionally vulnerable Dockerfile for Trivy learning

FROM python:3.9-slim

WORKDIR /app

# Install intentionally outdated packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    openssl \
    libssl-dev \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
