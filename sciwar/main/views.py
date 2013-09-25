from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from main.models import *
from django.utils import simplejson as json
import time
from datetime import datetime, timedelta

def main_page(request):
    today_events = Event.objects.filter(
            start_time__day = datetime.today().day + 0)\
    .order_by('start_time')
    current_event = Event.objects.filter(
            start_time__lte = datetime.now()).filter(
                    end_time__gte = datetime.now)
    if current_event:
        current_event_name = current_event[0].name
    else:
        current_event_name = ""

    events = {}
    for event in today_events:
        events[event.name] = event.start_time
    return render(request, 'index.html', {
        "state":_get_state(), "events":events,
        "current_event_name":current_event_name})

def info_page(request):
    return render(request, 'info.html', {"state":_get_state()})

def schedule_page(request):
    return render(request, 'schedule.html', {"state":_get_state()})

def map_page(request):
    return render(request, 'map.html', {"state":_get_state()})

def video_page(request):
    return render(request, 'video.html', {"state":_get_state()})

def update_information(request):
    avail_notice = True if request.GET.get('notice', False) == "true" else False
    avail_info = True if request.GET.get('information', False) == "true" else False

    contents = []
    informations = Info.objects.all()
    for info in informations:
        item = {
                'title': info.title,
                'article': info.content,
                'classify': info.get_category_display(),
                'date': info.time.strftime("%y.%m.%d")
                }
        if info.category == 1 and avail_notice:
            contents.append(item)
        if info.category == 2 and avail_info:
            contents.append(item)
    return HttpResponse(json.dumps({
        'contents': contents}, ensure_ascii=False, indent=4))

# private function
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
