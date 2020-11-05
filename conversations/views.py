from django.db.models import Q
from django.shortcuts import render
from users import models as user_models
from . import models


def go_conversation(request, host_pk, guest_pk):
    host = user_models.User.objects.get_or_none(pk=host_pk)
    guest = user_models.User.objects.get_or_none(pk=guest_pk)
    if host is not None and guest is not None:
        conversation = models.Conversation.objects.get(
            Q(participants=host) & Q(participants=guest)
        )
        if conversation is None:
            pass
