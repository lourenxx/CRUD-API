# CRUD FLASK API

> PROJECT STATUS: Concluded 

This is a basic Flask CRUD API that I made to study API concepts. This project uses Python, Flask, SQLite, and Docker.

You can clone this repo and run it in two different ways if you prefer: on your local machine or in a container.

> FOR BOTH WAYS, YOU NEED TO HAVE PIP INSTALLED ON YOUR MACHINE!!!


# RUN LOCALLY
To run the API on your local machine, it is advisable to create a Virtual Environment and place all the files in it. After that, download the "source/requirements.txt".


On Linux:
```
python -m venv /path/to/new/virtual/environment

cd source/

pip install requirements.txt
```

On Windows:
```
python -m venv c:\path\to\myenv

venv\Scripts\activate

cd source/

pip install requirements.txt
```

# RUN WITH DOCKER IMAGE

To run the API using Docker, you need to have Docker installed on your local machine. Once installed, follow these steps:

1- Access the API image on DockerHub and use the "docker pull" command to clone the image to your computer.

DockerHub image:
https://hub.docker.com/repository/docker/lourenxx/flask-api-image/tags

```
docker pull lourenxx/flask-api-image:v1.0
```

2-  After cloning the image, you need to run the container:

```
docker run -p 5000:5000 lourenxx/flask-api-image:v1.0
```



