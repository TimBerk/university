# Онлайн университет

Онлайн университет реализован на Django со связкой SQLite. В проекте имеется Makefile, который упростит первоначальную установку сайта.


## Installation

Перед запуском вам необходимо установить все зависимости. При работе с ОС Linux, в Makefile необходимо заменить python на python3.

```console
git clone https://github.com/TimBerk/university
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
* [Django environ’s](https://django-environ.readthedocs.io/en/latest/) - Django-environ allows to utilize 12factor inspired environment variables to configure Django application.
* [Django CKEditor](https://django-ckeditor.readthedocs.io/en/latest/) - Proven, enterprise-grade WYSIWYG HTML editor with wide browser compatibility, including legacy browsers.
* [Django eml email backend](https://github.com/kmike/django-eml-email-backend) - Django has filebased email backend that is handy for inspecting outgoing emails during development.
* [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/index.html) - The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.
* [Django RQ](https://github.com/rq/django-rq) - Django integration with RQ, a Redis based Python queuing library.

## Make команды

* **run** - запуск сервера разработки.
* **migrate** - синхронизация состояние базы данных с текущим состоянием моделей и миграций.
* **make-migrate** - создание новых миграции на основе изменений в моделях.
* **superuser** - создание администратора.
* **shell** - запуск интерактивного интерпретатора.
* **start** - инициализация тестовых данных.
* **static-files** - инициализация статических файлов.
* **rqscheduler** - запуск scheduler для Redis.
* **rqworker** - запуск worker для каждой указанной очереди Redis.


## Features

### Admin backend

### Users

* Sign in;
* Sign up;
* Profile editing(personal data).

### Courses

* Add category course, lessons, tasks.

### Contacts

* Sending letters with Redis.

## Demo User

```
Login: admin
Password: admin
```