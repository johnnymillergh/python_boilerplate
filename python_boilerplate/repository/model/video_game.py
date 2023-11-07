from peewee import CharField, DecimalField, IntegerField

from python_boilerplate.common.orm import peewee_table
from python_boilerplate.repository.model.base_model import BaseModel


@peewee_table
class VideoGame(BaseModel):
    title = CharField(max_length=200, null=False, index=True)
    handheld = IntegerField(null=True)
    max_players = IntegerField(null=True)
    multiplatform = IntegerField(null=True)
    online = IntegerField(null=True)
    genres = CharField(max_length=200, null=True)
    licensed = IntegerField(null=True)
    publishers = CharField(max_length=200, null=True)
    sequel = IntegerField(null=True)
    review_score = CharField(max_length=200, null=True)
    sales = DecimalField(null=True)
    used_price = DecimalField(null=True)
    console = CharField(max_length=200, null=True)
    rating = CharField(max_length=10, null=True)
    re_release = IntegerField(null=True)
    year = CharField(max_length=10, null=True)
