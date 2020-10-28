from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .inspection import Inspection
from .inspection_time import InspectionTime
from .inspection_confirmation import InspectionConfirmation