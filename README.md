# Online Survey

Online survey - Online survey for users
## Developer guide

In this repository you can find only Back-End & Dev-Ops source code.
The documentation of the web application can be found when starting the application by url
http://localhost/api/v1/docs

Used for Back-End:

* Python
* Django & Django Rest Framework.

## Setup Back-End

* Put .env to src/ by .env.Example (make sure you use DEBUG=True for local)
* ```python -m venv venv```
* ```source venv/bin/activate```
* ```pip install -r requirenments.txt```
* ```cd src```
* ```python manage.py makemigrations```
* ```python manage.py migrate```
* ```python manage.py createsuperuser```
* ```python manage.py runserver```


## Deployment
* Put .env to src/ by .env.Example (make sure you use DEBUG=False for local)
* ```sudo docker-compose -f docker-compose.yml -f docker-compose-dev.yml up ```
* ```sudo docker exec -it back python src/manage.py makemigrations ```
* ```sudo docker exec -it back python src/manage.py migrate ```
* ```sudo docker exec -it back python src/manage.py collectstatic ```
* ```sudo docker exec -it back python src/manage.py createsuperuser ```
* ```sudo docker-compose -f docker-compose.yml -f docker-compose-dev.yml down ```


So good luck!