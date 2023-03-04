from typing import Final

from loguru import logger
from peewee import SqliteDatabase

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


def configure():
    logger.warning(f"SQLite database created. Path: [{DATABASE_PATH}], {DATABASE}")
