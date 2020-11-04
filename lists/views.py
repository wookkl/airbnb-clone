from django.contrib import messages
from django.shortcuts import redirect, reverse
from rooms import models as room_models
from . import models


def toggle_room(request, room_pk):
    action = request.GET.get("action", None)
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    if room is not None and action is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My favorite Rooms"
        )
        if action == "add":
            the_list.rooms.add(room)
            messages.success(request, "Added Room")
        else:
            the_list.rooms.remove(room)
            messages.success(request, "Removed Room")
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))


def see_favs(request):
    pass