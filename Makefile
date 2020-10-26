run:
	python manage.py runserver
all:
	python manage.py runserver & cd frontend && npm run dev
migrate:
	python manage.py migrate
make-migrate:
	python manage.py makemigrations
remove-migrations:
	python manage.py remove-migrations
load-testusers:
	python manage.py update-test-users
superuser:
	python manage.py createsuperuser
shell:
	python manage.py shell
sql-shell:
	python manage.py debugsqlshell
static-files:
	python manage.py collectstatic
get-fixtures:
	python manage.py dumpdata courses --indent 4 > courses/fixtures/data.json
start:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py loaddata user/fixtures/group.json
	python manage.py create-admin --noinput --username admin --password admin --email admin@uni.ru
	python manage.py create-admin --noinput --username teacher --password teacher --email teacher@uni.ru --group teacher
	python manage.py create-admin --noinput --username student_1 --password student_1 --email student_1@uni.ru --group student
	python manage.py create-admin --noinput --username student_2 --password student_2 --email student_2@uni.ru --group student
	python manage.py update-test-users
	python manage.py loaddata user/fixtures/data.json
	python manage.py loaddata courses/fixtures/data.json
	python manage.py loaddata schedule/fixtures/data.json
	cd frontend && npm i
rqscheduler:
	python manage.py rqscheduler
rqworker:
	python manage.py rqworker default
get-packages:
	pip freeze > requirements.txt
install-packages:
	pip install -r requirements.txt
docker:
	docker-compose up -d
front:
	cd ./frontend && npm i && npm run build
build-front:
	cd ./frontend && npm run build