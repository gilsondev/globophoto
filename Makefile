configdb:
	@mysql -u root -p -e "CREATE DATABASE globophotos;GRANT ALL PRIVILEGES ON globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;FLUSH PRIVILEGES;"

syncdb:
	@python manage.py syncdb

migrate:
	@python manage.py migrate

run: configdb syncdb migrate
	@python manage.py runserver
