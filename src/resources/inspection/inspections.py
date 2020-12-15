from flask_restful import Resource
from util import parse_params
from repositories import InspectionRepository
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required


class InspectionsResource(Resource):
    @staticmethod
    @jwt_required
    def get():
        inspections = InspectionRepository.all()
        return [u.json for u in inspections]

    @staticmethod
    @parse_params(
        Argument("city", location="json", required=True, help="Missing parameter"),
        Argument("street", location="json", required=True, help="Missing parameter"),
        Argument("street_number", location="json", required=True, help="Missing parameter"),
        Argument("staircases", location="json", required=True, help="Missing parameter"),
        Argument("employee", location="json", required=True, help="Missing parameter")
    )
    @jwt_required
    def post(city: str, street: str, street_number: str, staircases: str, employee: str):
        inspection = InspectionRepository.create(city, street, street_number, staircases, employee)
        return inspection.json


