import threading
from datetime import datetime

from peewee import CharField, DateTimeField, TextField

from python_boilerplate.common.common_function import get_login_user
from python_boilerplate.common.orm import peewee_table
from python_boilerplate.repository.model.base_model import BaseModel


@peewee_table
class TraceLog(BaseModel):
    # called_by is inspect.stack()[1][3]
    called_by = CharField(max_length=200, null=False, index=True)
    function_qualified_name = CharField(max_length=200, null=False, index=True)
    function_arguments = TextField(null=True)
    thread = CharField(
        max_length=100, null=False, default=threading.current_thread().name, index=True
    )
    start_time = DateTimeField(null=False, default=datetime.now)

    # common 4 fields
    created_by = CharField(max_length=50, null=False, default=get_login_user)
    created_time = DateTimeField(null=False, default=datetime.now)
    modified_by = CharField(max_length=50, null=False, default=get_login_user)
    modified_time = DateTimeField(null=False, default=datetime.now)
