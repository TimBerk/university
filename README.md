# Онлайн университет

Онлайн университет реализован на Django со связкой SQLite. В проекте имеется Makefile, который упростит первоначальную установку сайта.


## Installation

Перед запуском вам необходимо установить все зависимости. При работе с ОС Linux, в Makefile необходимо заменить python на python3.

```console
git clone https://github.com/TimBerk/university
cd university
make install-packages
make make-migrate
make migrate
make start
make front
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
* [Django REST framework](https://www.django-rest-framework.org/) - Django REST framework is a toolkit for building Web APIs.
* [Django Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Simple JWT provides a JSON Web Token authentication backend.
* [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) - REST implementation of Django authentication system.
* [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) - library generates OpenAPI 2.0 documents.
* [Pipdeptree](https://github.com/naiquevin/pipdeptree) - command line utility for displaying the installed python packages in form of a dependency tree.
* [Django-filter](https://django-filter.readthedocs.io/en/stable/) - Django-filter is a generic, reusable application to alleviate writing some of the more mundane bits of view code.
* [Graphene-Python](https://graphene-python.org/) - library for building GraphQL APIs in Python.
* [Django braces](https://django-braces.readthedocs.io/en/latest/) - mixins for Django's class-based views.
* [Pendulum](https://pendulum.eustace.io/) - package to ease datetimes manipulation.
* [Django-cors-headers](https://github.com/adamchainz/django-cors-headers) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses.

## Make команды

* **run** - запуск сервера разработки.
* **all** - запуск сервера разработки с React.
* **migrate** - синхронизация состояние базы данных с текущим состоянием моделей и миграций.
* **make-migrate** - создание новых миграции на основе изменений в моделях.
* **remove-migrations** - удаление всех файлов миграций.
* **superuser** - создание администратора.
* **shell** - запуск интерактивного интерпретатора.
* **start** - инициализация тестовых данных.
* **static-files** - инициализация статических файлов.
* **rqscheduler** - запуск scheduler для Redis.
* **rqworker** - запуск worker для каждой указанной очереди Redis.
* **get-packages** - запись списка используемых пакетов в проекте.
* **install-packages** - установка необходимых пакетов для проекта.
* **front** - build frontend части для проекта.


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

### Schedule

* Add groups and schedule for them

### API

* Authorization with JWT token;
* CRUD for categories, courses and lessons.
* Auto generate OpenAPI 2.0 documents.

## Demo Users

```
administrator
Login: admin
Password: admin

teacher
Login: teacher
Password: teacher

student
Login: student_1
Password: student_1
```