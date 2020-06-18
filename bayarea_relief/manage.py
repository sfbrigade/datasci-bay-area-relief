import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_sqlalchemy import SQLAlchemy

from bayarea_relief import create_app


class Migration:
    def __init__(self, app, manager):
        self.app = app
        # TODO:  Create Environment variable
        url = "postgresql://postgres:postgres@localhost:5432/bar"
        self.app.config['SQLALCHEMY_DATABASE_URI'] = url

        # TODO: Create app settings class
        # app_settings = os.environ.['APP_SETTINGS']
        # self.app.config.from_object(os.environ['APP_SETTINGS'])
        self.db = SQLAlchemy(app)
        self.migrate = Migrate(app, self.db)
        self.manager = manager

    def run(self):
        self.manager.run()


def main():
    app = create_app()
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    migration = Migration(app, manager)
    migration.run()
