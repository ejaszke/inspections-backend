"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources import UserResource

USER_BLUEPRINT = Blueprint("user", __name__)

CORS(USER_BLUEPRINT)

Api(USER_BLUEPRINT).add_resource(
    UserResource, "/user/<string:name>"
)
