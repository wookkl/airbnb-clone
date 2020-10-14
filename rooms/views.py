from math import ceil
from django.shortcuts import render
from . import models as room_models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = room_models.Room.objects.all()[offset:limit]
    page_count = ceil(room_models.Room.objects.count() / 10)
    return render(
        request,
        template_name="rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
