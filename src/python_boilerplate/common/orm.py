from typing import TypeVar

from loguru import logger

from python_boilerplate.configuration.peewee_configuration import DATABASE
from python_boilerplate.repository.model.base_model import BaseModel

# `bound` argument forces that the type can be any subtype of BaseModel
T = TypeVar("T", bound=BaseModel)


def peewee_table(clazz: type[T]) -> type[T]:
    """
    The decorator to register peewee tables. Creates the table if not exists.

    Usage:
     * decorate a class with `@peewee_table`

    :param clazz: A subclass of `BaseModel`
    :return: A decorated class
    """
    logger.info(f"Registering peewee table: {clazz.__name__}")
    DATABASE.create_tables([clazz])
    return clazz
