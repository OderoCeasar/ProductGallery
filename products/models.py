from django.db import models
from django.db.models import FloatField
from mongoengine import Document, StringField, FileField

# Create your models here.
class Product(Document):
    name = StringField(required=True, max_length=100)
    description = StringField()
    price = FloatField(required=True)
    image = FileField()
