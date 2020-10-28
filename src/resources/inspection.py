from flask.json import jsonify
from flask_restful import Resource

from repositories import InspectionRepository
from transformers import InspectionTransformer


class InspectionResource(Resource):
    @staticmethod
    def get(id):
        inspection = InspectionRepository.find_by_id(id)
        return jsonify({"data": InspectionTransformer.transform(inspection)})
