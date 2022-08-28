from datetime import datetime

from peewee import DateTimeField

from python_boilerplate.repository.model.base.model import BaseModel, database


class StartupLog(BaseModel):
    """
    DetectedFace model
    """

    startup_time = DateTimeField(default=datetime.now)
    created_time = DateTimeField(default=datetime.now)
    modified_time = DateTimeField(default=datetime.now)


database.create_tables([StartupLog])
