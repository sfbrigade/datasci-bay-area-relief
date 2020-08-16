# bay-area-relief

## Running Project

1. Install [python3](https://www.python.org/downloads/)
2. Install a virtualenv

   ```bash
   pip3 install -U setuptools
   pip3 install virtualenv
   python3 -m venv env
   source env/bin/activate
   .\env\Scripts\activate (Windows Only)
   pip3 install --compile .[test]
   ```

   - To stop virtualenv then run this command `deactivate`

3. Run backend application and database `docker-compose up`
4. Use database with two ways:
   - Login `psql -d <database_name> -U <postgres username>` e.g. ` psql -d bar -U postgres
   - Using the [postgreSQL client](https://eggerapps.at/postico/) is easier and prefer
     - Credentials for your local postgres, should be in database.env
5. Stop application and database `docker-compose down`

## Running Migrations on your DB

1. Migrate and create tables `make upgrade-db`
2. If changes were made to model then follow these changes
   - Migrate first `make migrate-db`
   - Verify model changes in migrations/versions
   - Upgrade db `make upgrade-db`

## Run webserver with Docker

1. `docker build -t bay-area-relief .`
2. `docker run bay-area-relief`
3. `docker rmi bay-area-relief` (Optional)

### Install Postgres Client

- https://eggerapps.at/postico/

### Populate database

- `pip install psycopg2-binary sqlalchemy pandas`
- `python bayarea_relief/sheets_to_csv.py`
- `python bayarea_relief/ingest_raw_data.py -c data/ResultFile.csv`

### Initial Continuous Integration

Run unittests `make unittest`

## Troubleshooting

### Database

## Repo resources

- [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
- [Using form attribute for flask request](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
- [How to handle form data with flask](https://stackoverflow.com/questions/45590988/converting-flask-form-data-to-json-only-gets-first-value)
- [How to use postgress docker-compose](https://medium.com/analytics-vidhya/getting-started-with-postgresql-using-docker-compose-34d6b808c47c)
- [Flask SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
- [Learn about WSGI](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/)
