from flask_restful import Resource
from flask_jwt_extended import create_access_token
from util import parse_params
from flask_restful.reqparse import Argument
from repositories import UserRepository
from werkzeug.security import check_password_hash


class UserLoginResource(Resource):

    @staticmethod
    @parse_params(
        Argument("password", location="json", required=True, help="Missing parameter"),
        Argument("email", location="json", required=True, help="Missing parameter")
    )
    def post(email: str, password: str):
        user = UserRepository.find_by_email(email)
        if email != user.email or not check_password_hash(user.password, password):
            return {"message": "Bad username or password"}, 400
        access_token = create_access_token(identity=email)
        return {"access_token": access_token}, 200
