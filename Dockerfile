FROM python:3.7-slim-buster
WORKDIR /src
ENV FLASK_APP bayarea_relief/__main__.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8000
COPY bayarea_relief bayarea_relief/
COPY scripts scripts/
COPY setup.py .
RUN pip install --compile .
VOLUME ["/src/"]
EXPOSE 8000
CMD ["flask", "run"]