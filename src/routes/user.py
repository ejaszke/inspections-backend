"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.user import UserResource, UsersResources, UserLoginResource, UserMeResource

USER_BLUEPRINT = Blueprint("users", __name__)

CORS(USER_BLUEPRINT, resources={r"/api/*": {"origins": "https://inspections-frontend.herokuapp.com"}})

USER_BLUEPRINT = Blueprint("users", __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource, "/users/<string:id>"
),
Api(USER_BLUEPRINT).add_resource(
    UsersResources, "/users"
),
Api(USER_BLUEPRINT).add_resource(
    UserLoginResource, "/login"
),
Api(USER_BLUEPRINT).add_resource(
    UserMeResource, "/users/me"
)
