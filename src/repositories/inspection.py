from models import Inspection


class InspectionRepository:
    @staticmethod
    def all():
        return Inspection.query.all()

    @staticmethod
    def find_by_id(id):
        return Inspection.query.filter_by(id=id).one()

    @staticmethod
    def create(city, street, street_number, staircases, employee, flat_count):
        inspection = Inspection(city, street, street_number, staircases, employee, flat_count)
        return inspection.save()

    @staticmethod
    def update(inspection: Inspection, city, street, street_number, staircases, employee, flat_count):
        inspection.city = city
        inspection.street = street
        inspection.street_number = street_number
        inspection.staircases = staircases
        inspection.employee = employee
        inspection.flat_count = flat_count
        return inspection.save()

    @staticmethod
    def delete(inspection: Inspection):
        return inspection.delete()
