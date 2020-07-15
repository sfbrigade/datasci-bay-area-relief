from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from bayarea_relief import app, db


class Migration:
    def __init__(self, app, manager, db):
        self.app = app
        self.db = db
        # TODO: Create app settings class
        # app_settings = os.environ.['APP_SETTINGS']
        # self.app.config.from_object(os.environ['APP_SETTINGS'])
        self.migrate = Migrate(self.app, self.db, compare_type=True)
        self.manager = manager

    def run(self):
        self.manager.run()


def main():
    from bayarea_relief import models
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    migration = Migration(app, manager, db)
    migration.run()
