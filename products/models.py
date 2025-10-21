from django.db import models
from mongoengine import Document, StringField, FileField, FloatField

# Create your models here.
class Product(Document):
    name = StringField(required=True, max_length=100)
    description = StringField(required=True, max_length=255)
    price = FloatField(required=True)
    image = FileField(required=False)
