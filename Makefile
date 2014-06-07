PROJECT_NAME := globophoto

.PHONY: clean configdb syncdb migrate run test pep8

clean:
	find . -name "*.pyc" -delete

configdb:
	@mysql -u root -p -e "CREATE DATABASE globophotos;GRANT ALL PRIVILEGES ON globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;GRANT ALL PRIVILEGES ON test_globophotos.* TO 'globophoto'@'localhost' IDENTIFIED BY 'globophoto' WITH GRANT OPTION;FLUSH PRIVILEGES;"
	@echo 'Created user globophoto and database globophotos.'

syncdb:
	@python manage.py syncdb

migrate:
	@python manage.py migrate

run: configdb clean syncdb migrate
	@python manage.py runserver

test: clean pep8
	python manage.py test $(APP)

pep8: clean
	@pep8 --show-source --show-pep8 $(PROJECT_NAME)
