from bootiful_sanic.bootiful_sanic import app
from bootiful_sanic.plugin.opentracing import setup_opentracing
from bootiful_sanic.util import sanic_config_manager


setup_opentracing(app=app)


sanic_config_manager(app, prefix="SANIC_")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port="8000", debug=True)
