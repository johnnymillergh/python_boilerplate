from typing import Type

from loguru import logger

from python_boilerplate.configuration.peewee_configuration import DATABASE
from python_boilerplate.repository.model.base_model import BaseModel


def peewee_table(clazz: Type[BaseModel]) -> Type[BaseModel]:
    """
    The decorator to register peewee tables. Creates the table if not exists.

    Usage:
     * decorate a class with `@peewee_table`

    :param clazz: a class
    """

    logger.info(f"Registering peewee table: {clazz.__name__}")
    DATABASE.create_tables([clazz])
    return clazz
