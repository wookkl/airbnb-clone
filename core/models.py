from django.db import models
from . import managers


class AbstractTimeStamp(models.Model):

    """ TimeStamped Model Definifion """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True
