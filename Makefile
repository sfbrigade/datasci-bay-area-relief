# this is the target
unittest:
	pip3 install --compile [test].
	flake8 .
	pytest
database-start:
	docker-compose up -d
	docker exec -it $$(docker ps -aqf "name=postgres") /bin/bash
database-stop:
	docker-compose down
database-remove:
	docker-compose down
	docker kill $(docker ps -aqf "name=postgres")
	docker volume rm $(docker volume ls |  grep bayarea-relief-volume)
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