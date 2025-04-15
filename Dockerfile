# Use an official Python image as a base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 to access the Flask app from outside the container
EXPOSE 5000

# Default command to run the Flask application
CMD ["python", "app.py", "--host=0.0.0.0"]
