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
            start_time__lte = datetime.now()).filter(\
            end_time__gte = datetime.now())

    other_events = Event.objects.all().order_by('start_time')
    if current_event:
        current_event = current_event[0]
        other_events = other_events.exclude(id = current_event.id)
    else:
        current_event = []

    players = []
    kaist_players = current_event.kaist_players.all()
    postech_players = current_event.postech_players.all()

    current_time = datetime.now()
    return render(request, 'index.html', {
        "state":_get_state(),\
        "today_events":today_events,\
        "current_event":current_event,\
        "other_events":other_events,\
        "current_time":current_time,\
        "kaist_players":kaist_players,\
        "postech_players":postech_players,\
    })

def info_page(request):
    return render(request, 'info.html', {"state":_get_state()})

def schedule_page(request):
    Month = [0,"JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    current_time = datetime.now()
    date = Month[current_time.month]+" "+str(current_time.day)
    events = _get_schedule()
    num = 0
    for index,event in enumerate(events):
        if event["date"] == date:
            num=index+1

    return render(request, 'schedule.html', {"state":_get_state(), "events":_get_schedule(), "today_date":num})

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
                'date': info.time.strftime("20%y. %m. %d.")
                }
        if info.category == 1 and avail_notice:
            contents.append(item)
        if info.category == 2 and avail_info:
            contents.append(item)
    return HttpResponse(json.dumps({
        'contents': contents}, ensure_ascii=False, indent=4))


def update_video(request):
    classify = request.GET.get('name','all')
    sort_order = int(request.GET.get('order', 0))

    event_set = []
    if classify == "etc":
        event_set.append("HACKING CONTEST")
        event_set.append("OPENING CEREMONY")
        event_set.append("BEER PARTY")
        event_set.append("CLOSING CEREMONY")
    elif classify != "all":
        event_set.append(classify)
    
    contents = []
    if sort_order == 1:
        videos = Video.objects.all().order_by('time')
    else:
        videos = Video.objects.all().order_by('-time')
    for video in videos:
        if classify=="all" or video.event.name in event_set:
            item = {
                'title': video.name,
                'event': video.event.name,
                'link': video.link,
                'time': video.time.strftime("20%y. %m. %d. %H:%M")
                }
            contents.append(item)
    return HttpResponse(json.dumps({
        'contents': contents}, ensure_ascii=False, indent=4))

def detail_page(request, event_id):
    event = Event.objects.get(id = event_id)
    kaist_players = event.kaist_players.all()
    postech_players = event.postech_players.all()

    if event.start_time <= datetime.now() and event.end_time >= datetime.now():
        is_live = True
    else:
        is_live = False

    return render(request, 'detail.html', {
        "state":_get_state(),\
        "is_live":is_live,\
        "event":event,\
        "kaist_players":kaist_players,\
        "postech_players":postech_players,\
    })

# private function
def _get_state():
    state = {}
    events_list = Event.objects.all()

    state["KAIST"] = 0
    state["POSTECH"] = 0
    state["ALL"] = len(events_list)
    state["DONE"] = 0
    for event in events_list:
        if event.winner == 1:
            state["KAIST"] += event.score
        elif event.winner == 2:
            state["POSTECH"] += event.score
        if event.end_time < datetime.now():
            state["DONE"] += 1
    
    return state

def _get_schedule():
    Month = [0,"JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    events = []
    events_list = sorted(Event.objects.all(), key=lambda k: k.start_time)
    exist_date = []
    for event in events_list:
        if not event.start_time.date() in exist_date:
            exist_date.append(event.start_time.date())
    for date in exist_date:
        events_per_day = []
        for event in events_list:
            if event.start_time.date() == date:
                info = {}
                info["id"] = event.id
                info["name"]= event.name
                info["start_time"] = event.start_time
                info["end_time"] = event.end_time
                info["location"] = event.building
                events_per_day.append(info)
        events.append({"date":Month[date.month]+" "+str(date.day), "events":events_per_day})
    return events

