from flask.json import jsonify
from flask_restful import Resource

from models import InspectionConfirmation
from repositories import InspectionRepository
from transformers import InspectionTransformer


class InspectionsResource(Resource):
    @staticmethod
    def get():
        inspections = InspectionRepository.all()
        return jsonify({"data": [InspectionTransformer.transform(inspection) for inspection in inspections]})

    @staticmethod
    def post():
        inspection = InspectionRepository.create('City', 'Street', '23', '1-12')
        inspection.confirmations.append(InspectionConfirmation('Yes', 'Test'))
        inspection.save()
        return jsonify({"data": InspectionTransformer.transform(inspection)})
