# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
