from django.contrib import admin
from . import models


@admin.register(models.Reservations)
class ReservationAdmin(admin.ModelAdmin):

    """ Revervation Admin Definition """

    pass
