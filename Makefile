# this is the target
unittest:
	docker build -t dev-bar .
	docker images | grep dev-bar
	docker rmi dev-bar
application-start:
	docker-compose up -d
#	docker exec -it $$(docker ps -aqf "name=postgres") /bin/bash
application-stop:
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