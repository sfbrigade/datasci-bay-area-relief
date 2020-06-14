# this is the target
unittest:
	docker build -t bayarea-relief .
	docker run bayarea-relief
start-env:
	pip3 install virtualenv
	python3 -m venv env
	source env/bin/activate
stop-env:
	deactivate
webserver:
	pip3 install -r requirements.txt
	python -m bay_area_relief