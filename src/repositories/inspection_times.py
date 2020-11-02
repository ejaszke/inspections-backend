from models import InspectionTime


class InspectionTimeRepository:
    @staticmethod
    def find_by_id(id: str):
        return InspectionTime.query.filter_by(id=id).one()
