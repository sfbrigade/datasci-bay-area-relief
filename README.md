# bay-area-relief 


### Running Project
1. Install [python3](https://www.python.org/downloads/)
2. Install a virtualenv
    ```
    1. pip3 install virtualenv
    2. python3 -m venv env
    3. source env/bin/activate
    4. pip3 install --compile .[test]
    ```
    * To stop virtualenv then run this command `deactivate`
3. Run backend webserver `webserver`

#### Running Database
1. Start postgres db `make database-start`
    * Login `psql -d <database_name> -U <postgres username>` e.g. ` psql -d bar -U postgres
    * Using the [postgreSQL client](https://eggerapps.at/postico/) is easier and prefer
        * Credentials for your local postgres, should be in database.env
2. Stop postgres db `make database-stop`

#### Running Migrations on your DB 
1. Migrate and create tables `make upgrade-db`
2. If changes were made to model then follow these changes
    * Migrate first `make migrate-db`
    * Verify model changes in migrations/versions
    * Upgrade db `make upgrade-db`


### Initial Continuous Integration
2. Run unittests `make unittest`


### Repo resources 
* [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
* [Using form attribute for flask request](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
* [How to handle form data with flask ](https://stackoverflow.com/questions/45590988/converting-flask-form-data-to-json-only-gets-first-value)
* [How to use postgress docker-compose](https://medium.com/analytics-vidhya/getting-started-with-postgresql-using-docker-compose-34d6b808c47c)
* [Flask SQL Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
