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
static-files:
	python manage.py collectstatic
start:
	python manage.py create-admin --noinput --username admin --password admin --email admin@admin.ru
	python manage.py loaddata user/fixtures/data.json
	python manage.py loaddata courses/fixtures/data.json
	python manage.py collectstatic
rqscheduler:
	python manage.py rqscheduler
rqworker:
	python manage.py rqworker default
get-packages:
	pip freeze > requirements.txt
install-packages:
	pip install -r requirements.txt