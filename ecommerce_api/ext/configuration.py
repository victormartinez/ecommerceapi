from importlib import import_module


def load_extensions(app):
    for extension in app.config["EXTENSIONS"]:
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext, factory)(app)


def load_blueprints(app):
    for extension in app.config["BLUEPRINTS"]:
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext, factory)(app)


def load_middlewares(app):
    for middleware in reversed(app.config["MIDDLEWARES"]):
        module_name, klass = middleware.split(":")
        ext = import_module(module_name)
        app.wsgi_app = getattr(ext, klass)(app.wsgi_app)


def init_app(app, settings_override=None):
    app.config.from_object("settings")
    if settings_override:
        app.config.update(settings_override)
