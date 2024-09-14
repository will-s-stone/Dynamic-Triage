# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . /app

# Expose the port your Flask app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["poetry", "run", "flask", "run"]
