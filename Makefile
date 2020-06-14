# this is the target
unittest:
	docker build -t bayarea-relief .
	docker run bayarea-relief
