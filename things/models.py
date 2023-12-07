from django.db import models
from django.db.models import Model


class Thing(Model):
    name = models.CharField()
    description = models.TextField()
    quantity = models.IntegerField()
    