# Import all the models, so that Base has them before being
# imported by Alembic

from backend.db.base_class import Base

from .models.user import *
