from loguru import logger

from python_boilerplate.repository.model.base_model import DATABASE


def peewee_table(clazz):
    """
    The decorator to register peewee tables. Creates the table if not exists.

    Usage:
     * decorate a class with `@peewee_table`

    :param clazz: a class
    """

    logger.info(f"Registering peewee table: {clazz.__name__}")
    DATABASE.create_tables([clazz])
    return clazz
