from app import create_app
from flask_script import Manager,Server
from app import db
from app.models import registration, blogs,coments, contacts, newslater
from flask_migrate import Migrate, MigrateCommand


app = create_app('production')


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,registration = registration,blogs = blog, coments = coments, contacts = contacts)


if __name__ == '__main__':
    app.run()
    # manager.run()