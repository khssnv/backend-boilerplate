# Import all the models, so that Base has them before being
# imported by Alembic

from {{cookiecutter.project_slug}}.db.base_class import Base

from .models.user import *
