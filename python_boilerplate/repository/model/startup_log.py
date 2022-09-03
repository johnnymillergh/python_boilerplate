from datetime import datetime

from peewee import CharField, DateTimeField, TextField

from python_boilerplate.repository.model.base.model import BaseModel, database


class StartupLog(BaseModel):
    """
    Startup Log
    """

    current_user = CharField(max_length=50, null=False)
    host = CharField(max_length=50, null=False)
    command_line = TextField(null=False)
    startup_time = DateTimeField(default=datetime.now)
    created_time = DateTimeField(default=datetime.now)
    modified_time = DateTimeField(default=datetime.now)


database.create_tables([StartupLog])
