# Use Python base image
FROM python:3.9

# Install system dependencies (IMPORTANT FIX)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]