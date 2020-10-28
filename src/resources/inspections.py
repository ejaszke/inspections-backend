from flask.json import jsonify
from flask_restful import Resource

from repositories import InspectionRepository
from transformers import InspectionTransformer


class InspectionsResource(Resource):
    @staticmethod
    def get():
        inspections = InspectionRepository.all()
        return jsonify({"data": [InspectionTransformer.transform(inspection) for inspection in inspections]})
