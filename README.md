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
git clone https://github.com/hcourt/minicert.git
```

### ... with Docker
```console
docker-compose up
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
### with Docker
```console
CONFIG_ENV=production docker-compose up
```

### without Docker
Run the server
```console
python manage.py runserver --settings=minicert.settings.production
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

#### with Docker
```console
CONFIG_ENV=development docker-compose up
```


#### without Docker
Run a dummy http server for certificate authority mocking.  We use 
[httpbin](httpbin.org).
```console
sudo docker run -p 80:80 kennethreitz/httpbin
```
Run the server
```console
python manage.py runserver
```
