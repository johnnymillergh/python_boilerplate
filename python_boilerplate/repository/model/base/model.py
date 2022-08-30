import os

from loguru import logger
from peewee import Model, SqliteDatabase

from python_boilerplate.function_collection import get_data_dir, get_module_name

_db_path: str = f"{get_data_dir()}{os.path.sep}{get_module_name()}.db"
database: SqliteDatabase = SqliteDatabase(_db_path)
logger.warning(f"SQLite database created. Path: {_db_path}, {database}")


class BaseModel(Model):
    """
    Base model for persistence.
    Models and Fields https://docs.peewee-orm.com/en/latest/peewee/models.html#model-inheritance
    """

    class Meta:
        database = database
        legacy_table_names = False
