from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from main.models import *
from django.utils import simplejson as json

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
                'date': info.time.strftime("20%y. %m. %d")
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
        event_set.append("OPENING CONTEST")
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
                'time': video.time.strftime("20%y. %m. %d %H:%M")
                }
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
