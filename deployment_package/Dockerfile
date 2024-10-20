# Use an official Python runtime as the base image
FROM python:3.12
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install AWS CLI
RUN apt-get update && \
    apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the required packages
RUN pip install --no-cache-dir boto3 aws-sam-cli

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the application when the container launches
CMD ["sam", "local", "start-api", "--host", "0.0.0.0"]
