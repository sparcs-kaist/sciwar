from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from main.models import *

def main_page(request):
    return render(request, 'index.html', {"state":_get_state()})

def info_page(request):
    return render(request, 'info.html', {"state":_get_state()})

def schedule_page(request):
    return render(request, 'schedule.html', {"state":_get_state()})

def map_page(request):
    return render(request, 'map.html', {"state":_get_state()})

def video_page(request):
    return render(request, 'video.html', {"state":_get_state()})

def _get_state():
    state = {}
    events_list = Event.objects.all()

    state["KAIST"] = 0
    state["POSTECH"] = 0
    state["ALL"] = len(events_list)
    state["DONE"] = state["ALL"]
    for event in events_list:
        if event.winner == 1:
            state["KAIST"] += event.score
        elif event.winner == 2:
            state["POSTECH"] += event.score
        else:
            state["DONE"] -= 1
    
    return state
