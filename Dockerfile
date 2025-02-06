# Use a lightweight Python base image
FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask scikit-learn pickle-mixin

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
