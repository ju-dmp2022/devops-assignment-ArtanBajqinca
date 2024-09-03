# Use the official image as a parent image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the calculator.py file executable
RUN chmod +x calculator.py

# Define the command to run the application when the container starts
ENTRYPOINT ["python", "calculator.py"]