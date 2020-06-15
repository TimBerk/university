run:
	python manage.py runserver
migrate:
	python manage.py migrate
make-migrate:
	python manage.py makemigrations
superuser:
	python manage.py createsuperuser
shell:
	python manage.py shell
start:
	python manage.py create-admin --noinput --username admin --password admin --email admin@admin.ru
	python manage.py loaddata user/fixtures/data.json
	python manage.py loaddata courses/fixtures/data.json