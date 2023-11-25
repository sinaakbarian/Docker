# Docker

This repository serves as a guide to Docker implementation and understanding.

## Summary of the 3-Hour Video
For a comprehensive overview, check out the [3-hour video](https://www.youtube.com/watch?v=3c-iBn73dDE).

## What is a Container?
A container is a way to package an application with all necessary dependencies and configurations. Containers reside in a container repository, such as Docker Hub, where you can find official and non-official container images. Using containers eliminates the need to install packages in the operating system, promoting consistency across team members.

Containers stack images on top of each other. The base image is typically the Linux OS, and on top of it, application images are layered.

### Docker Image vs. Container
- **Docker Image**: An artifact that is stationary.
- **Docker Container**: The image in action. Running containers can be viewed using `docker ps`.

### Docker vs. Virtual Machine
Docker images are smaller and faster than virtual machines since they lack an OS kernel. Containers only have what's necessary, making them efficient.

### Common Docker Commands
- `docker pull <package>`: Install Docker image (e.g., `docker pull redis`).
- `docker images`: Check images on the system.
- `docker run <package>`: Pull and start a container.
- `docker ps`: List all running containers.
- `docker stop <container_id>`: Stop a running container.
- `docker start <container_id>`: Start a stopped container.
- `docker ps -a`: Show all running or non-running containers.
- `docker run <package>:<version>`: Specify the version when running a container.
- `docker run -d <package>`: Run a container in detach mode.
- `docker exec -it <container_id> /bin/bash`: Access an interactive terminal of a running container.

### Connecting Ports
- To bind host ports to a laptop: `docker run -p <our_port>:<host_port> <package>`.

### Naming Containers
- Use `--name` to name containers for easier identification.

### Docker Compose
- Organize with a `.yaml` file (Docker Compose file).
- Use `docker-compose -f <name.yaml> up` to start services defined in the Compose file.
- Use `docker-compose down` to shut down services.

## Building and Testing Code with Docker
1. Develop code.
2. Test using Docker.
3. Commit with CI (e.g., Jenkins).

### Dockerfile
To build a Docker image, create a Dockerfile:
```Dockerfile
FROM node
ENV NODE_ENV=production
RUN mkdir -p /home/app
COPY ./home/app
CMD ["node", "server.js"]
```

### Build an Image
- `docker build -t <tag> .`: Build an image in the current directory.

## Private Repositories with Amazon ECR
1. Create an Elastic Container Registry (ECR) in AWS.
2. Push to a private repository:
   - `docker login` (AWS command).
   - Tag the image: `docker tag <image> <registryDomain>/<imageName>:<tag>`.
   - Push the image: `docker push <registryDomain>/<imageName>:<tag>`.

## Deployment
Add your app to a YAML file, specifying the image. Perform `docker login` before deployment.

## Docker Volumes
When saving data, use:
- `-v <folder_mount>` or `-v <name>:<address>`.
- In Docker Compose, define volumes in the YAML file.
