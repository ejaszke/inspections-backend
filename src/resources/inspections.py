from flask_restful import Resource

from models import InspectionConfirmation
from repositories import InspectionRepository
from mappers import InspectionMapper


class InspectionsResource(Resource):
    @staticmethod
    def get():
        inspections = InspectionRepository.all()
        return {"data": [InspectionMapper.transform(inspection) for inspection in inspections]}

    @staticmethod
    def post():
        inspection = InspectionRepository.create('City', 'Street', '23', '1-12')
        inspection.confirmations.append(InspectionConfirmation('Yes', 'Test'))
        inspection.save()
        return {"data": InspectionMapper.transform(inspection)}
