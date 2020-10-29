from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from repositories import UserRepository


class UserMeResource(Resource):

    @jwt_required
    def get(self):
        # return 'authorized resource'
        # Access the identity of the current user with get_jwt_identity
        current_user_email = get_jwt_identity()
        user = UserRepository.find_by_email(current_user_email)
        return user.json
