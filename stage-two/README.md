Simple Person CRUD API
=======================

This is a simple REST API capable of performing CRUD operations on a "person" resource. The API interfaces with sqlite database (an inbuilt django file-based datatbase) and allows dynamic parameter handling for operations based on person names. The project is hosted on GitHub and includes UML diagrams, setup instructions, and sample API usage.

Table of Contents
==================

- Installation
- Usage
- API Endpoints
- Database Modeling


Installation
--------------

* To set up and run the API locally, follow these steps:

    - Clone the GitHub repository: git clone `https://github.com/TessyJames28/HNG/tree/main/stage-two`
    - Install the required dependencies: ``pip -r install requirements.txt``
    - To use sqlite database, ``uncomment`` database configured for ``sqlite`` and ``comment`` the second one
    - ``cd`` into ``crud/simplerestapi`` folder
    - ``Configure`` the ``database``: ``python manage.py makemigrations``
    - ``Migrate``: ``python manage.py migrate``
    - ``Run`` the API server: ``python manage.py runserver``

* The API will be accessible at ``http://localhost:8000/api``


Usage
------

* To use the API, you can send HTTP requests to the provided endpoints using any API testing tool or client.

API Endpoints
-------------
* The API provides the following endpoints for ``CRUD`` operations on the "person" resource:

    - ``POST`` ``/api`` - Create a new person
    - ``GET`` ``/api/<user_id>`` - Retrieve details of a person
    - ``PUT`` ``/api/<user_id>`` - Update details of a person
    - ``DELETE`` ``/api/<user_id>`` - Delete a person


Database Modeling
------------------

The database structure can be represented using UML diagrams. The diagram showcases the relationships and structure of the API's classes and models. Please refer to the UML diagram provided in the repository.

![UML Diagram](stage-two/crud/UML_ERD.png)