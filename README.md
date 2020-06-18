# bay-area-relief 


### Running Project
1. Install [python3](https://www.python.org/downloads/)
2. Install virtualenv `make start-env`
3. Run backend webserver `make webserver`
4. pip install --compile .

#### Running Database
1. Start postgresQL `make database-start`
    * Login `psql -d <database_name> -U <postgres username>` e.g. ` psql -d bar -U postgres
`
2. Stop postgresQL `make database-stop`



### Initial Continuous Integration
1. Install [docker engine](https://docs.docker.com/engine/install/)
2. Run unittests `make unittest`


### Repo resources 
* [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
* [Using form attribute for flask request](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
* [How to handle form data with flask ](https://stackoverflow.com/questions/45590988/converting-flask-form-data-to-json-only-gets-first-value)
* [How to use postgress docker-compose](https://medium.com/analytics-vidhya/getting-started-with-postgresql-using-docker-compose-34d6b808c47c)
