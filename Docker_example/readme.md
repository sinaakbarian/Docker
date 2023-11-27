# Machine Learning Example with Docker

This repository contains a simple machine learning project that uses linear regression to estimate a number. The project is containerized using Docker for easy deployment and reproducibility.

## Docker Setup

To run this project in a Docker container, follow these steps:

### 1. Create Dockerfile

Create a Dockerfile (`Dockerfile.txt`) with the following content:

```Dockerfile
# Use official Python image for the runtime environment
FROM python:3.9

# Create a working environment
RUN mkdir /home/app/
COPY . /home/app/

# Set the working directory
WORKDIR /home/app/

# Install requirements
RUN pip install -r requirements.txt

# Run the code
CMD ["python", "main.py"]
```

### 2. Build Docker Image

Build the Docker image by running the following command in the terminal:

```bash
docker build -f Dockerfile.txt -t name:version path/to/file
```

Replace `name:version` with your desired image name and version, and ensure you specify the correct path to your Dockerfile.

### 3. Run Docker Container

Once the Docker image is built, you can run the container using the following command:

```bash
docker run name:version
```

If your code requires terminal interaction, use the `-it` flag:

```bash
docker run -it name:version
```

This will start the containerized application, and you can interact with it as needed.

## Project Structure

- **main.py**: The main Python code implementing linear regression for number estimation.

- **requirements.txt**: File containing Python dependencies required for the project.

Feel free to modify the code in `main.py` and update the dependencies in `requirements.txt` according to your project requirements.

