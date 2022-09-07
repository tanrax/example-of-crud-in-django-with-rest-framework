# Example of CRUD in Django with REST FRAMEWORK

- Live Demo.
- Endpoint Get List Books.
- Endpoint Get Details Book.
- Endpoint Add Book.
- Endpoint Update Book.
- Endpoint Delete Book.
- All Endpoints contain your test.

## Live Demo

### Get list

``` shell
curl  localhost:8000/api/book/
```

Output

``` json
[
    {
        "id": 1,
        "title": "Things Fall Apart",
        "country": "Nigeria",
        "year": 1958,
        "author": "Chinua Achebe",
        "created_at": "2021-07-15T14:27:14.927177",
        "updated_at": "2021-07-15T14:27:14.927213"
    },
    {
        "id": 2,
        "title": "Fairy tales",
        "country": "Denmark",
        "year": 1836,
        "author": "Hans Christian Andersen",
        "created_at": "2021-07-15T14:27:14.930223",
        "updated_at": "2021-07-15T14:27:14.930233"
    },
   ... 
```

### Get Detail

``` shell
curl localhost:8000/api/book/1/
```

Output

``` json
{
    "id": 1,
    "title": "Things Fall Apart",
    "country": "Nigeria",
    "year": 1958,
    "author": "Chinua Achebe",
    "created_at": "2021-07-15T14:27:14.927177",
    "updated_at": "2021-07-15T14:27:14.927213"
}
```

### Create

``` shell
curl -XPOST -H "Content-type: application/json" -d '{"title": "The foundation", "country": "eeuu", "author": "Isaac Asimov", "year": "1951"}' localhost:8000/api/book/
```

Output

``` json
{
  "id": 101,
  "title": "The foundation",
  "country": "eeuu",
  "year": 1951,
  "author": "Isaac Asimov",
  "created_at": "2021-07-15T14:47:25.262738",
  "updated_at": "2021-07-15T14:47:25.262753"
}
```

### Update

``` shell
curl -XPUT -H "Content-type: application/json" -d '{"title": "The End of Eternity", "country": "eeuu", "author": "Isaac Asimov", "year": "1955"}' localhost:8000/api/book/1/
```

Output

``` json
{
  "id": 1,
  "title": "The End of Eternity",
  "country": "eeuu",
  "year": 1955,
  "author": "Isaac Asimov",
  "created_at": "2021-07-15T14:47:25.262738",
  "updated_at": "2021-07-15T14:50:47.697224"
}
```

### Delete

``` shell
curl -XDELETE localhost:8000/api/book/1/
```

Output

``` json
{
  "id": null,
  "title": "The End of Eternity",
  "country": "eeuu",
  "year": 1955,
  "author": "Isaac Asimov",
  "created_at": "2021-07-15T14:47:25.262738",
  "updated_at": "2021-07-15T14:50:47.697224"
}
```

### Ping

``` shell
curl localhost:8000/ping/
```

Output

``` json
{"ping": "pong!"}
```

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

## Fake data

``` bash
python3 manage.py runscript create_books
```

## Test

``` bash
pytest
```
