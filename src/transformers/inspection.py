from models import Inspection, InspectionTime, InspectionConfirmation


class InspectionTransformer:
    @staticmethod
    def transform(inspection: Inspection):
        return {
            "id": inspection.id,
            "city": inspection.city,
            "street": inspection.street,
            "street_number": inspection.street_number,
            "staircases": inspection.staircases,
            "times": [InspectionTransformer.transform_time(time) for time in inspection.times],
            "confirmations": [
                InspectionTransformer.transform_confirmation(confirmation) for confirmation in inspection.confirmations
            ]
        }

    @staticmethod
    def transform_time(time: InspectionTime):
        return { }

    @staticmethod
    def transform_confirmation(confirmation: InspectionConfirmation):
        return {
            "id": confirmation.id,
            "answer": confirmation.answer,
            "additional_notes": confirmation.additional_notes
        }
