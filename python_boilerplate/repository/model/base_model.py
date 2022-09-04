from typing import Final

from loguru import logger
from peewee import Model, SqliteDatabase

from python_boilerplate.common.common_function import get_data_dir, get_module_name

# Database https://docs.peewee-orm.com/en/latest/peewee/database.html
# Recommended Settings https://docs.peewee-orm.com/en/latest/peewee/database.html#recommended-settings
# Logging queries https://docs.peewee-orm.com/en/latest/peewee/database.html#logging-queries

DATABASE_PATH: Final = get_data_dir() / f"{get_module_name()}.db"
DATABASE: Final = SqliteDatabase(
    DATABASE_PATH,
    pragmas={
        # WAL-mode. https://sqlite.org/wal.html
        "journal_mode": "wal",
        # 64MB cache.
        "cache_size": 64 * -1024,
        # Let the OS manage syncing.
        "synchronous": 0,
    },
)
logger.warning(f"SQLite database created. Path: [{DATABASE_PATH}], {DATABASE}")


class BaseModel(Model):
    """
    Base model for persistence.
    Models and Fields https://docs.peewee-orm.com/en/latest/peewee/models.html#model-inheritance
    Field types table https://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table
    """

    class Meta:
        """
        Model configuration is kept namespaced in a special class called Meta. This convention is borrowed from Django.
        Meta configuration is passed on to subclasses, so our project’s models will all subclass BaseModel.
        There are many different attributes you can configure using Model.Meta.

        Model options and table metadata
        https://docs.peewee-orm.com/en/latest/peewee/models.html#model-options-and-table-metadata
        Primary Keys, Composite Keys and other Tricks
        https://docs.peewee-orm.com/en/latest/peewee/models.html#primary-keys-composite-keys-and-other-tricks
        """

        database = DATABASE
        legacy_table_names = False
