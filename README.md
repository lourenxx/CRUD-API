# CRUD FLASK API

> PROJECT STATUS: Concluded 

This is a basic Flask CRUD API that I made to study the API's concepts. This project uses Python, Flask SQLite and Docker.

You can clone this repo and run it in two different aways if you preffer: In your local machine or in a container.

> FOR THE BOTH AWAYS YOU NEED TO HAVE PIP INSTALLED IN YOU MACHINE!!!


# RUN LOCAL
To run the api in your local machine, is advisible that you create a Virtual Environment and put all the archives in it, after that you download the "source/requirement.txt".


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

# RUN WITH DOCKER CONTAINER

For run the api using Docker, you need to have it installed in your local machine, with it, open the linux or wsl terminal and wrote this commands:

```
docker build -t image_name .

docker run -p 5000:5000 image_name
```

