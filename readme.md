# CRUD with Django Rest Framework

## Description
Showcasing Rest Framework with a virtual store.

Store has Products and Category models. A product has name, price, amount in stock and category.

There are views in store/views.py responsible for CRUD operations with Rest Framework.

## Usage
Clone the repo in your local machine and go to the project. Then run in terminal:
````
python manage.py migrate
````

Run server with:
````
python manage.py runserver
````
and access admin page on - http://127.0.0.1:8000/ to access startpage with product listing and new product creation links.
To access detail/update/delete pages, it's necessary to use url http://127.0.0.1:8000/ +url defined in store.urls.py/

## Requirements
- Python 3.12

To install other requirements run in terminal:
````
pip install -r requirements.txt
````
