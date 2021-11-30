from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from leaderboard.models import Participant


def home_view(request):
    participant_queryset = Participant.objects.order_by('points')
    context = {
        "participant_list": participant_queryset,
    }
    HTML_STRING = render_to_string('home-view.html', context = context)
    return HttpResponse(HTML_STRING)

