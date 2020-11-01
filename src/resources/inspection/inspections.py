from flask_restful import Resource

from models import InspectionConfirmation
from repositories import InspectionRepository


class InspectionsResource(Resource):
    @staticmethod
    def get():
        inspections = InspectionRepository.all()
        return [u.json for u in inspections]

    @staticmethod
    def post():
        inspection = InspectionRepository.create('City', 'Street', '23', '1-12')
        inspection.confirmations.append(InspectionConfirmation('Yes', 'Test'))
        inspection.save()
        return inspection.json
