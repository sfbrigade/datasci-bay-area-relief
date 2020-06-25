# this is the target
unittest:
	pip3 install --compile .[test]
	flake8 . --max-line-length=88 --exclude migrations/
	pytest
database-start:
	docker-compose up -d
	docker exec -it $$(docker ps -aqf "name=postgres") /bin/bash
database-stop:
	docker-compose down
webserver:
	pip3 install --compile .
	webserver
migrate-db:
	pip3 install --compile .
	migrate db init
	migrate db migrate
upgrade-db:
	make migrate-db
	migrate db upgrade
downgrade-db:
	make migrate-db
	migrate db downgrade