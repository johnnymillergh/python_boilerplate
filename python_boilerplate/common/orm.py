from loguru import logger

from python_boilerplate.repository.model.base_model import DATABASE


def peewee_table(clazz):
    logger.info(f"Registering peewee table: {clazz.__name__}")
    DATABASE.create_tables([clazz])
    return clazz
