from models import Inspection
from models import InspectionTime
from models import InspectionConfirmation


class InspectionRepository:
    @staticmethod
    def all():
        return Inspection.query.all()

    @staticmethod
    def find_by_id(id):
        return Inspection.query.filter_by(id=id).one()

    @staticmethod
    def create(city, street, street_number, staircases):
        inspection = Inspection(city, street, street_number, staircases)
        return inspection.save()
