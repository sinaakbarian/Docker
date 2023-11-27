# GitHub Container Registry - Docker Image Push

This guide outlines the steps to push a Docker image to the GitHub Container Registry using the GitHub Package feature. This enables the release and distribution of Docker images through GitHub. 

## Prerequisites

Before pushing the Docker image to the GitHub Container Registry, ensure the following prerequisites are met:

1. **GitHub Token**: Obtain a GitHub token with the necessary permissions for pushing Docker images to the GitHub Container Registry.

## Steps

### 1. Docker Login

Use the following command to authenticate with Docker using your GitHub token:

```bash
docker login --username <username> --password <github_token> ghcr.io
```

Replace `<username>` with your GitHub username and `<github_token>` with your GitHub token.

### 2. Tagging the Docker Image

Tag the Docker image with the GitHub Container Registry repository information:

```bash
docker tag <appname>:<version> ghcr.io/<username>/<appname>:<version>
```

Replace `<appname>` with the name of your Docker image, `<version>` with the desired version, and `<username>` with your GitHub username.

### 3. Pushing the Docker Image

Push the tagged Docker image to the GitHub Container Registry:

```bash
docker push ghcr.io/<username>/<appname>:<version>
```

Replace `<username>`, `<appname>`, and `<version>` with the corresponding values used in the tagging step.

## Conclusion

Following these steps will allow you to successfully push your Docker image to the GitHub Container Registry using the GitHub Package feature. Ensure that you have the necessary permissions and authentication credentials to perform these actions.
