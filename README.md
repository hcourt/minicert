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
 [Git](https://git-scm.com/),
 [Python (3.6+)](https://www.python.org/downloads/),
 [pip](https://pip.pypa.io/en/stable/installing/),
  and [virtualenv](https://virtualenv.pypa.io/en/latest/)
 installed.

In development, minicert uses a SQLite (3.8.3+) database for simplicity.

In production, minicert uses PostgreSQL for scale, but any
 SQL database can be used instead. See Django's documentation on
 [database setup](https://docs.djangoproject.com/en/2.2/topics/install/#get-your-database-running).


## Getting Started

Clone the repository
```console
git clone https://github.com/hcourt/minicert.git
```

Start a virtualenv
```console
$ python -m venv ~/.virtualenvs/minicertenv

$ source ~/.virtualenvs/minicertenv/bin/activate
```

Install requirements
```console
$ pip install -r requirements/py3.txt
```

## Production
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
Run a dummy http server for certificate authority mocking.  We use 
[httpbin](httpbin.org).
```console
sudo docker run -p 80:80 kennethreitz/httpbin
```

Run the server
```console
python manage.py runserver
```
