FROM python:3.9-slim

LABEL authors="williamstone"

# Install build dependencies
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libhdf5-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry==1.8.0

WORKDIR /app

# Copy the Poetry configuration and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

# Copy the application code
COPY . .

# Set the entrypoint
ENTRYPOINT ["top", "-b"]

