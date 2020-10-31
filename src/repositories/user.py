from models import User


class UserRepository:

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def create(email: str, password: str):
        user = User(email=email, password=password)
        return user.save()

    @staticmethod
    def find_by_email(email: str):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_id(_id: str):
        return User.query.filter_by(id=_id).one()
