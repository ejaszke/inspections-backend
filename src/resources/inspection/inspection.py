from flask_restful import Resource

from repositories import InspectionRepository


class InspectionResource(Resource):
    @staticmethod
    def get(id):
        inspection = InspectionRepository.find_by_id(id)
        return inspection.json
