from django.db import models


class AbstractTimeStamp(models.Model):

    """ TimeStamped Model Definifion """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True