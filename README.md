# Example of CRUD in Django with REST FRAMEWORK

All endpoints contain your test.

## Endpoints

- /api/books	GET
_ /api/books	POST
- /api/books/:pk	GET
- /api/books/:pk	DELETE
- /api/books/:pk	PUT

## Install

``` bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
```

## Run

``` bash
python3 manage.py runserver
```
