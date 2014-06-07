.PHONY: clean configdb syncdb migrate run test

clean:
	find . -name "*.pyc" -delete

configdb:
	@mysql -u root -p -e "CREATE DATABASE globophotos;GRANT ALL PRIVILEGES ON globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;GRANT ALL PRIVILEGES ON test_globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;FLUSH PRIVILEGES;"
	@echo 'Created user globophoto and database globophotos.'

syncdb:
	@python manage.py syncdb

migrate:
	@python manage.py migrate

run: configdb syncdb migrate
	@python manage.py runserver

test:
	python manage.py test $(APP)
