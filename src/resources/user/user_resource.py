from flask_restful import Resource
from repositories import UserRepository
from flask import render_template
from flask_weasyprint import HTML, render_pdf
from flask_jwt_extended import jwt_required

class UserResource(Resource):

    # @staticmethod
    # @swag_from("../swagger/user/GET.yml")
    # def get(name):
    #     """ Return an pdf """
    #     html = render_template('sample.html', name=name)
    #     return render_pdf(HTML(string=html))

    @staticmethod
    @jwt_required
    def get(id: str):
        user = UserRepository.find_by_id(id)
        return user.json
