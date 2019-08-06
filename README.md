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

This documentation assumes you have Git, Python (3.5+), pip, virtualenv, and 
Django (2.2+) installed.  If you don't, follow these instructions:

TODO

Minicert uses a SQLite (3.8.3+) database for simplicity, but any SQL database can be used
 instead. See Django's documentation on [database setup](https://docs.djangoproject.com/en/2.2/topics/install/#get-your-database-running).

## Getting Started

Clone the repository

Start a virtualenv
```console
$ python -m venv ~/.virtualenvs/minicertenv

$ source ~/.virtualenvs/minicertenv/bin/activate
```

Install requirements
```console
$ pip install -r requirements/py3.txt
```

Run the server
```console
python manage.py runserver
```

## Development

Create database migrations for model updates
```console
$ python manage.py makemigrations app
```
Run migrations against the database
```console
$ python manage.py migrate
```
Start a shell
```console
$ python manage.py shell
```
