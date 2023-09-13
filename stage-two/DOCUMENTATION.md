API Documentation
==================

* This document provides detailed documentation for the ``Simple Person CRUD API``. It outlines the:
    - request/response formats
    - setup instructions
    - sample API usage.

Table of Contents
==================

- API Endpoints
- Request/Response Formats
- Setup and Installation


API Endpoints
---------------

* The ``API`` provides the following endpoints for ``CRUD`` operations on the "person" resource:

    - ``POST`` ``/api`` - Create a new person
    - ``GET`` ``/api/<user_id>`` - Retrieve details of a person
    - ``PUT`` ``/api/<user_id>`` - Update details of a person
    - ``DELETE`` ``/api/<user_id>`` - Delete a person


Request/Response Formats
-------------------------


* Create a new person ``(POST /api)``

Request:
---------
- Endpoint: ``POST /api``
- Content-Type: ``application/json``

```
{
  "name": "John Doe"
}
```

Response: 
----------

- HTTP/1.1 201 Created
- Content-Type: application/json

```
{
    "id": 1,
    "name": "John Doe"
}
```

* if ``name is not a string``:
  - HTTP/1.1 400 Bad Request

```
{
    "name": [
        "Name must be a string"
    ]
}
```

* if request body is missing:
  - HTTP/1.1 400 Bad Request

```
{
    "name": [
        "This field is required."
    ]
}
```


Get a User
-----------

* Retrieve details of a person ``(GET /api/<user_id>)``

Request:
---------

- Endpoint: ``GET /api/<user_id>``


Response:
-----------

- HTTP/1.1 200 OK
- Content-Type: application/json

```
{
  "id": "1,
  "name": "John Doe"
}
```


* If the user with the ``id`` is not found:
```
{
    "detail": "User does not exist"
}
```

Update a User
--------------

* Update details of a person ``(PUT /api/<user_id>)``

Request:
---------

- Endpoint: ``PUT /api/<user_id>``
- Content-Type: application/json

```
{
  "name": "Jane Doe"
}
```

Response:
----------

- HTTP/1.1 200 OK
- Content-Type: application/json

```
{
  "id": 1,
  "name": "Jane Doe"
}
```

Delete a User
--------------

* Delete a person ``(DELETE /api/<user_id>)``

Request:
---------

- Endpoint: ``DELETE /api/<user_id>``

Response:
----------

- HTTP/1.1 204 No Content


Setup and Installation
-----------------------

* To set up and run the API locally, follow these steps:

    - Clone the GitHub repository: git clone `https://github.com/TessyJames28/HNG/tree/main/stage-two`
    - Install the required dependencies: ``pip -r install requirements.txt``
    - To use sqlite database, ``uncomment`` database configured for ``sqlite`` and ``comment`` the second one
    - ``cd`` into ``crud/simplerestapi`` folder
    - ``Configure`` the ``database``: ``python manage.py makemigrations``
    - ``Migrate``: ``python manage.py migrate``
    - ``Run`` the API server: ``python manage.py runserver``

* The API will be accessible at ``http://localhost:8000/api``