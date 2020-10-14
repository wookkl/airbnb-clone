from django.shortcuts import render

# Create your views here.


def all_rooms(request):
    return render(request, template_name="all_rooms.html")
