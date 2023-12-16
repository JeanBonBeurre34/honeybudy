# honeybudy

## Overview

This project simulates a honeypot using a fake Unix system. It's designed to attract and deceive attackers by mimicking a Unix-like command-line interface, logging interactions for monitoring purposes.
Prerequisites

Before you begin, ensure you have Docker installed on your system. You can download and install Docker from Docker's official website.

## Getting Started

### Clone the Repository

First, clone this repository to your local machine using:

```bash
git clone https://github.com/JeanBonBeurre34/honeybudy
```


## Building the Docker Image

To build the Docker image, run the following command in the project directory:

```bash
docker build -t my-honeypot .
```

This command builds a Docker image named my-honeypot based on the Dockerfile in your current directory.
Running the Docker Container

Once the image is built, you can run the Docker container using:

```bash
docker run -p 2222:2222 my-honeypot
```

This command starts a container instance of your honeypot. It forwards port 2222 from your host machine to port 2222 in the Docker container, where the honeypot application is listening.

## Interacting with the Honeypot

You can interact with the honeypot by connecting to port 2222 on your localhost. For example, using a tool like telnet or netcat, you can connect via:

```bash
telnet localhost 2222
```

```bash
nc localhost 2222
```

## Viewing the Logs

To view the logs of interactions with the honeypot, follow these steps:

### Find the Container ID

First, find the ID of your running Docker container:

```bash
docker ps
```

### Access the Container's Shell

Access the shell of the Docker container:

```bash
docker exec -it [container-id] /bin/bash
```
Replace **[container-id]** with your container's ID.


### View the Log File

Inside the container, view the log file:

```bash
cat honeypot_logs.txt

```

### Stopping the Container

To stop the running Docker container, you can use the following command:

```bash
docker stop [container-id]
```
Replace **[container-id]** with the ID of your running Docker container. You can find the container ID by running docker ps.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
