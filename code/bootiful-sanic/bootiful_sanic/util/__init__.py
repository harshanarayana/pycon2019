from os import environ, path

from gino.ext.sanic import Gino
from sanic_limiter import Limiter, get_remote_address

from sanic import Sanic


def sanic_config_manager(app: Sanic, prefix: str = "SANIC_", env_file="../../.env"):
    for variable, value in environ.items():
        if variable.startswith(prefix):
            _, key = variable.split(prefix, 1)
            app.config[key] = value
    if env_file and path.isfile(env_file):
        try:
            with open(env_file) as fh:
                data = fh.read()
            for line in data.split("\n"):
                var, value = line.split("=")
                var = var.replace(prefix, "")
                app.config[var] = value
        except:
            pass


def setup_database_creation_listener(app: Sanic, database: Gino):
    database.init_app(app)

    @app.listener("after_server_start")
    async def setup_database(app: Sanic, loop):
        await database.gino.create_all()


def setup_rate_limiter(app: Sanic):
    limiter = Limiter(
        app,
        global_limits=["1000/hour", "100/second"],
        key_func=get_remote_address,
        strategy="moving-window",
        storage_uri="memory://",
    )

    return limiter
