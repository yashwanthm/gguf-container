# Use RHEL UBI 8 base image
FROM registry.access.redhat.com/ubi8/python-38

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Run the application
CMD ["python", "serve.py"]
