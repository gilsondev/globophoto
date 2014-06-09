PROJECT_NAME := globophoto

.PHONY: clean configdb syncdb migrate createsuperuser run test pep8

clean:
	find . -name "*.pyc" -delete

configdb:
	@echo 'Set root password to config database...'
	-@mysql -u root -p -e "CREATE DATABASE globophotos;GRANT ALL PRIVILEGES ON globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;GRANT ALL PRIVILEGES ON test_globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;FLUSH PRIVILEGES;"
	@echo 'Created user globophoto and database globophotos.'

syncdb:
	@python manage.py syncdb --noinput

migrate:
	@python manage.py migrate

createsuperuser:
	@python manage.py createsuperuser

run: configdb clean syncdb migrate createsuperuser
	@python manage.py runserver

test: clean pep8
	python manage.py test $(APP)

pep8: clean
	@pep8 --show-source --show-pep8 --exclude=migrations $(PROJECT_NAME)
