# this is the target
unittest:
	flake8 . --max-line-length=88 --exclude migrations/
	pytest
database-start:
	docker-compose up -d
#	docker exec -it $$(docker ps -aqf "name=postgres") /bin/bash
database-stop:
	docker-compose down
init-migrate-db:
	migrate db init
	migrate db migrate
upgrade-db:
	migrate db upgrade
downgrade-db:
	migrate db downgrade