from flask_restful import Resource

from repositories import InspectionRepository
from mappers import InspectionMapper


class InspectionResource(Resource):
    @staticmethod
    def get(id):
        inspection = InspectionRepository.find_by_id(id)
        return {"data": InspectionMapper.transform(inspection)}
