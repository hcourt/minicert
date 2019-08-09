# minicert

A tiny identity and certificate management API, written in Django.

This API supports:
- **Creating/Deleting Customers**
- **Creating Certificates**
- **Listing all of a Customer’s Active Certificates**
- **Activating/Deactivating Certificates.** If a certificate is either activated
 or de-activated, it can notify an external system (via an HTTP call) about that
 fact.
- **Persistence** (data is stored in a DB and survives computer restarts)

## Prerequisites

This documentation assumes you have
 [Docker](https://www.docker.com/products/docker-desktop) and
 [Git](https://git-scm.com/) installed.
 
Depending on your usecase, you may also want
 [Python (3.6+)](https://www.python.org/downloads/),
 [pip](https://pip.pypa.io/en/stable/installing/),
  and [virtualenv](https://virtualenv.pypa.io/en/latest/)
 installed.

In development, minicert uses a SQLite (3.8.3+) database for simplicity.

In production, minicert uses PostgreSQL for scale, but any
 SQL database can be used instead. See Django's documentation on
 [database setup](https://docs.djangoproject.com/en/2.2/topics/install/#get-your-database-running).

## Scaling minicert

This API and associated docker application have the following scaling properties
- In production, the PostgreSQL database scales to terabytes of data.
- In development, the SQLite database scales to gigabytes of data.
- Because the main application runs in a single container on a single host 
 behind the nginx container, it may not scale well with the number of concurrent
 requests.  In production this application should be multiplexed behind a load
 balancer.
- The backing data stores are limited by the size of the host.  If you run
 the PostgreSQL container on a small host, it will fill up your disk quickly. 
 In a scaled production setting, the database should be located on dedicated 
 hosts.


## Getting Started

Clone the repository
```console
$ git clone https://github.com/hcourt/minicert.git
```

### ... with Docker
```console
$ docker-compose up
```

### ... without Docker
Start a virtualenv
```console
$ python -m venv ~/.virtualenvs/minicertenv

$ source ~/.virtualenvs/minicertenv/bin/activate
```

Install requirements
```console
$ pip install -r requirements/py3.txt
```

## Web App
Visit the Django console for the API at http://localhost:8000/api/

## Production
### ... with Docker
```console
$ CONFIG_ENV=production docker-compose up
```

### ... without Docker
Run the server
```console
$ python manage.py runserver --settings=minicert.settings.production
```

## Development

### Database changes
Create database migrations for model updates
```console
$ python manage.py makemigrations app
```
Run migrations against the database
```console
$ python manage.py migrate
```

### Shell
Start a python shell in the Django environment
```console
$ python manage.py shell
```

### Run a development build

#### ... with Docker
```console
$ CONFIG_ENV=development docker-compose up
```


#### ... without Docker
Run a dummy http server for certificate authority mocking.  We use 
[httpbin](httpbin.org).
```console
$ sudo docker run -p 80:80 kennethreitz/httpbin
```
Run the server
```console
$ python manage.py runserver
```


## API Specification
You are encouraged to visit the API via a browser.  The UI makes it simple to
 navigate between endpoints.
 
The examples below are accomplished with `curl`, but you could visit these
 in-browser as well.
### Index
#### `/api/`
_Allowed: OPTIONS, GET_

List all API endpoints

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/
```
 ```json
{
  "customer_list": "http://localhost:8000/api/customers/",
  "customer_index": "http://localhost:8000/api/customer/1/",
  "customer_certificates": "http://localhost:8000/api/customer/1/certs/",
  "customer_active_certificates": "http://localhost:8000/api/customer/1/active-certs/",
  "certificates": "http://localhost:8000/api/certificates/",
  "certificate_index": "http://localhost:8000/api/certificate/1/",
  "certificate_activate": "http://localhost:8000/api/certificate/1/activate/"
}
```

</details>

### Customers
#### `/api/customers/`
_Allowed: GET, HEAD, OPTIONS_

List all certificates

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/customers/
```
```json
[
    {
        "id": 1,
        "name": "Jane Smith",
        "email": "jane.smith@cloudflare.com",
        "password": "pbkdf2_sha256$150000$Aucc0qAMptVW$bFp3p9kb7sNN5fnNbPdkFG+I4nnzWyGO1lWkrxrHnyA="
    }
]
```

</details>

#### `/api/customer/<int:pk>`
_Allowed: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS_

Perform CRUD operations on customers.

All attributes are readable.  Passwords are stored hashed, and are viewable only
 as such.

All attributes are writable.  Passwords are hashed before storing.

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/customer/1/
```
```json
{
    "id": 1,
    "name": "Jane Smith",
    "email": "jane.smith@cloudflare.com",
    "password": "pbkdf2_sha256$150000$Aucc0qAMptVW$bFp3p9kb7sNN5fnNbPdkFG+I4nnzWyGO1lWkrxrHnyA="
}
```

</details>

#### `/api/customer/<int:pk>/certs/`
_Allowed: GET, HEAD, OPTIONS_

List all certificates owned by a customer.

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/customer/1/certs/
```

```json
{
    "results": [
        {
            "id": 1,
            "private_key": "<memory at 0x7fcec77efdc8>",
            "active": true,
            "cert_body": "this-is-a-cert-body",
            "customer": 1
        }
    ]
}
```

</details> 

#### `/api/customer/<int:pk>/active-certs/`
_Allowed: GET, HEAD, OPTIONS_

List all certificates owned by a customer.

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/customer/1/active-certs/
```
```json
{
    "results": [
        {
            "id": 1,
            "private_key": "<memory at 0x7fcec77efdc8>",
            "active": true,
            "cert_body": "this-is-a-cert-body",
            "customer": 1
        }
    ]
}
```

</details> 

### Certificates
#### `/api/certificates/`
_Allowed: GET, HEAD, OPTIONS_

List all certificates

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/certificates/
```
```json
[
    {
        "id": 1,
        "private_key": "<memory at 0x7fcec77efe88>",
        "active": true,
        "cert_body": "this-is-a-cert-body",
        "customer": 1
    }
]
```

</details>

#### `/api/certificate/<int:pk>`
_Allowed: GET, POST, HEAD, OPTIONS_

Perform CRD operations on certificates.

All attributes are readable.  Private keys are binary blobs and are rendered to
 strings.

No attributes are writable.  To update a certificate's `active` state, see
 `/api/certificate/<int:pk>/activate`.

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/certificate/1/
```
```json
{
    "id": 1,
    "private_key": "<memory at 0x7fcec77efe88>",
    "active": true,
    "cert_body": "this-is-a-cert-body",
    "customer": 1
}
```

</details>

#### `/api/certificate/<int:pk>/activate/`
_Allowed: PUT, PATCH, OPTIONS_

Activate or deactivate a certificate.

<details> <summary>Example</summary>

```console
$ curl http://localhost:8000/api/certificate/1/activate
```
```json
{
    "id": 1,
    "private_key": "<memory at 0x7fcec77efe88>",
    "active": true,
    "cert_body": "this-is-a-cert-body",
    "customer": 1
}
```
```json
{
    "active": true
}
```
</details>
