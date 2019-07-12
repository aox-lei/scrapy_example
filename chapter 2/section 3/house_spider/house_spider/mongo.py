# -*- coding: utf-8-*-
from mongoengine import Document, IntField, StringField, FloatField


class House(Document):
    title = StringField(max_length=255)
    total_price = IntField()
    area = StringField(max_length=32)
    direction = StringField(max_length=32)
    community = StringField(max_length=32)
    url = StringField(max_length=255)

class Community(Document):
    name = StringField(max_length=255)
    address = StringField(max_length=255)
    area = StringField(max_length=255)