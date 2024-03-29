from sanic_openapi import doc

from sanic.blueprints import Blueprint
from sanic.response import json


health = Blueprint("health", url_prefix="/health")


@health.route("/status")
@doc.summary("Health Status API")
@doc.produces({"status": str})
async def health_status_swagger(request):
    return json({"status": "OK"})
