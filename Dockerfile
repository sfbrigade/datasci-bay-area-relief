FROM python:3.7-slim-buster
WORKDIR /src
COPY bayarea_relief bayarea_relief/
COPY setup.py .
COPY tests tests/
COPY .flake8 .
COPY pytest.ini .
RUN pip install --compile .[test]
RUN flake8 . --max-line-length=88 --exclude migrations/ && pytest


FROM python:3.7-slim-buster
WORKDIR /src
COPY bayarea_relief bayarea_relief/
COPY setup.py .
RUN pip install --compile .
EXPOSE 8000
EXPOSE 5000
CMD ["gunicorn",  "-w 4" ,"-b 0.0.0.0:8000",  "bayarea_relief:app"]