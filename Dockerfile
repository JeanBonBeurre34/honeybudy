# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY givemethehoney.py .

# Make port 2222 available to the world outside this container
EXPOSE 2222

# Run honeypot.py when the container launches
CMD ["python", "./givemethehoney.py"]
