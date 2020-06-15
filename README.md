# Онлайн университет

Онлайн университет реализован на Django со связкой SQLite. В проекте имеется Makefile, который упростит первоначальную установку сайта.


## Installation

Перед запуском вам необходимо установить все зависимости.

```console
git clone --recursive https://github.com/TimBerk/university
cd university
pip install -r requirements.txt
make make-migrate
make migrate
make start
```

## Built With

* [Django](https://www.djangoproject.com/) -  web framework written in Python.
* [Django autoslug](https://django-autoslug.readthedocs.org/) - Django library that provides an improved slug field.
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library.

## Make команды

* **run** - запуск сервера разработки.
* **migrate** - синхронизация состояние базы данных с текущим состоянием моделей и миграций.
* **make-migrate** - создание новых миграции на основе изменений в моделях.
* **superuser** - создание администратора.
* **shell** - запуск интерактивного интерпретатора.
* **start** -  инициализация тестовых данных.


## Features

### Admin backend

### Users

* Sign in;
* Sign up;
* Profile editing(personal data).

### Courses

* Add category course, lessons, tasks.

## Demo User

```
Login: admin
Password: admin
```