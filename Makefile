m:
	./manage.py makemigrations
	./manage.py migrate
u:
	./manage.py createsuperuser
c:
	./manage.py collectstatic
r:
	./manage.py runserver
ta:
	./manage.py test applications/account
tp:
	./manage.py test applications/product
tf:
	./manage.py test applications/favorite