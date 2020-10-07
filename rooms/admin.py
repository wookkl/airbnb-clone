from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ ItemAdmin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Romm Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "baths",
        "bedrooms",
        "check_in",
        "cehck_out",
        "instant_book",
    )
    list_filter = (
        "instant_book",
        "city",
        "country",
    )
    search_fields = ("city", "^host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ PhotoAdmin Definition """

    pass
