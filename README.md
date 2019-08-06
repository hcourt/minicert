# minicert

A tiny identity and certificate management API, written in Django.

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