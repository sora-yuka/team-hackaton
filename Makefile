m:
	./manage.py makemigrations
	./manage.py migrate
u:
	./manage.py createsuperuser
c:
	./manage.py collectstatic
r:
	./manage.py runserver
t:
	python3 task.py