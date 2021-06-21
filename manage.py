from flask_script import Manager, Shell

from ecommerce_api.app import create_app

app = create_app()


def _make_context():
    return dict(app=app, db=db, models=models)


manager = Manager(app, db)
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
