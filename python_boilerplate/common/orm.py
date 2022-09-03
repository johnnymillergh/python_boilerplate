from loguru import logger

from python_boilerplate.repository.model.base_model import database


def peewee_table(clazz):
    logger.info(f"Registering peewee table: {clazz.__name__}")
    database.create_tables([clazz])
    return clazz
