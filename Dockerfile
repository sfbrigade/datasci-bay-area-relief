FROM python:3.7-slim-buster
WORKDIR /usr/src/app
COPY bayarea_relief bayarea_relief/
COPY scripts scripts/
COPY setup.py .
RUN pip install --compile .
ENTRYPOINT ["webserver"]