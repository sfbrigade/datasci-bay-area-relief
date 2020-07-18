# this is the target
unittest:
	flake8 . --max-line-length=88 --exclude migrations/ && pytest
application-start:
	docker-compose up -d
#	docker exec -it $$(docker ps -aqf "name=postgres") /bin/bash
application-start:
	docker-compose down
init-migrate-db:
	migrate db init
	migrate db migrate
upgrade-db:
	migrate db migrate
	migrate db upgrade
downgrade-db:
	migrate db downgrade
test-terraform:
	export AWS_PROFILE=codesf && aws s3 ls