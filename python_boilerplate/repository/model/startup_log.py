import os
import platform
from datetime import datetime

from peewee import CharField, DateTimeField, TextField

from python_boilerplate.common.common_function import get_login_user
from python_boilerplate.common.orm import peewee_table
from python_boilerplate.repository.model.base_model import BaseModel


@peewee_table
class StartupLog(BaseModel):
    """
    Startup Log
    """

    current_user = CharField(
        max_length=50, null=False, default=get_login_user, index=True
    )
    host = CharField(max_length=50, null=False, default=platform.node, index=True)
    command_line = TextField(null=False)
    current_working_directory = TextField(null=False, default=os.getcwd)
    startup_time = DateTimeField(null=False, default=datetime.now)
    exit_time = DateTimeField(null=True)

    # common 4 fields
    created_by = CharField(max_length=50, null=False, default=get_login_user)
    created_time = DateTimeField(null=False, default=datetime.now)
    modified_by = CharField(max_length=50, null=False, default=get_login_user)
    modified_time = DateTimeField(null=False, default=datetime.now)

    class Meta:
        # `indexes` is a tuple of 2-tuples, where the 2-tuples are
        # a tuple of column names to index and a boolean indicating
        # whether the index is unique or not.
        indexes = (
            # create a non-unique on current_user and host
            (("current_user", "host"), False),
        )
