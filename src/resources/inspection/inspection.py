from flask_restful import Resource
from repositories import InspectionRepository
from flask_restful.reqparse import Argument
from util import parse_params
from flask_jwt_extended import jwt_required


class InspectionResource(Resource):
    @staticmethod
    def get(id):
        inspection = InspectionRepository.find_by_id(id)
        return inspection.json

    @staticmethod
    @jwt_required
    def delete(id: str):
        inspection = InspectionRepository.find_by_id(id)
        if not inspection:
            return {"message": "Not found"}, 404
        else:
            inspection.delete()

    @staticmethod
    @parse_params(
        Argument("city", location="json", required=True, help="Missing parameter"),
        Argument("street", location="json", required=True, help="Missing parameter"),
        Argument("street_number", location="json", required=True, help="Missing parameter"),
        Argument("staircases", location="json", required=True, help="Missing parameter"),
        Argument("employee", location="json", required=True, help="Missing parameter"),
        Argument("flat_count", location="json", required=True, help="Missing parameter"),
    )
    @jwt_required
    def put(id: str, city: str, street: str, street_number: str, staircases: str, employee: str, flat_count: int):
        inspection = InspectionRepository.find_by_id(id)
        if not inspection:
            return {"message": "Not found"}, 404
        else:
            inspection = InspectionRepository.update(
                inspection,
                city,
                street,
                street_number,
                staircases,
                employee,
                flat_count
            )
            return inspection.json
