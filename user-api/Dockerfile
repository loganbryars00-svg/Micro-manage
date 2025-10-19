# Use lightweight Python image
FROM python:3.12-slim
# Set working directory
WORKDIR /app
# Copy requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy application code
COPY . .
# Command to run the application
CMD ["python", "app.py"]