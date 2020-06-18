FROM python:3.7-slim
WORKDIR /usr/app/src
COPY requirements.txt .
COPY bayarea_relief bay_area_relief/
COPY tests/ tests/
COPY pytest.ini .
COPY .flake8 .
RUN pip install -r requirements.txt
CMD flake8 && pytest