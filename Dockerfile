FROM python:3.7-slim-buster
WORKDIR /src
ENV FLASK_APP bayarea_relief/__main__.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8000
COPY bayarea_relief bayarea_relief/
COPY setup.py .
COPY tests tests/
RUN pip install --compile .[test]
EXPOSE 8000
CMD ["flask", "run"]