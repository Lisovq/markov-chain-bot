from models import db_models
from models.db import Database


def db_create_models() -> None:
    Database.create_tables(db_models)
