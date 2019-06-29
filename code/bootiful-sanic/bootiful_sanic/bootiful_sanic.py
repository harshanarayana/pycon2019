from bootiful_sanic.blueprint.health import health
from bootiful_sanic.blueprint.user import user
from bootiful_sanic.model import DATABASE
from bootiful_sanic.util import (
    setup_database_creation_listener,
    setup_rate_limiter,
)
from sanic_openapi import doc, swagger_blueprint

from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)

limiter = setup_rate_limiter(app)


app.blueprint(swagger_blueprint)

app.blueprint(health)

app.blueprint(user)
setup_database_creation_listener(app, DATABASE)


@app.route("/")
async def default(request):
    return json({"message": "hello Sanic!"})
