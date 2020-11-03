from flask_restful import Resource
from werkzeug.security import generate_password_hash
from flask_restful.reqparse import Argument
from util import parse_params
from repositories import UserRepository
from flask_jwt_extended import jwt_required


class UsersResources(Resource):

    @staticmethod
    @jwt_required
    def get():
        users = UserRepository.get_all()
        return [u.json for u in users]

    @staticmethod
    @parse_params(
        Argument("password", location="json", required=True, help="Missing parameter"),
        Argument("email", location="json", required=True, help="Missing parameter")
    )
    @jwt_required
    def post(email: str, password: str):
        if UserRepository.find_by_email(email):
            return {"message": "Email already exits"}, 400
        else:
            user = UserRepository.create(
                email=email, password=generate_password_hash(password)
            )
        return user.json
