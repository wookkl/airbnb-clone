from django.shortcuts import render
from django.core.paginator import Paginator
from . import models as room_models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page")
    room_list = room_models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(
        request,
        template_name="rooms/home.html",
        context={
            "rooms": rooms,
        },
    )
