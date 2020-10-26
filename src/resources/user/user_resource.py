from flask_restful import Resource
from repositories import UserRepository
from flask import render_template
from flask_weasyprint import HTML, render_pdf


class UserResource(Resource):

    # @staticmethod
    # @swag_from("../swagger/user/GET.yml")
    # def get(name):
    #     """ Return an pdf """
    #     html = render_template('sample.html', name=name)
    #     return render_pdf(HTML(string=html))

    @staticmethod
    def get(user_id: int):
        user = UserRepository.find_by_id(user_id)
        return {"user": user.json}
