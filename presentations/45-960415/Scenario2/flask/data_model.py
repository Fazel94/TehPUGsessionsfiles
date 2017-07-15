from mongoengine import Document
from mongoengine.fields import (IntField, StringField)

class DataModel(Document):

    # id = IntField(default=148290)
    text = StringField(required=True)

    meta = {'collection': 'texts'}
