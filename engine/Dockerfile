FROM python:3.9

# Install dependencies for h5py (HDF5 and other required libraries)
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*


RUN pip install poetry

COPY . .

RUN poetry install

ENV FLASK_APP=engine

# Expose the Flask port
EXPOSE 5000

# Run Flask app
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]



