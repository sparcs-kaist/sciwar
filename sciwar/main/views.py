from django.http import HttpResponse
from django.shortcuts import render
from django.db import models

def main_page(request):
    return render(request, 'index.html')

def info_page(request):
    return render(request, 'info.html')

def schedule_page(request):
    return render(request, 'schedule.html')

def map_page(request):
    return render(request, 'map.html')

def video_page(request):
    return render(request, 'video.html')

def _get_kaist_total_score():
    kaist_total = 0
    events_list = Event.objects.all()

    for event in events_list:
        if event.event_is_finished:
            if kaist_score > postech_score:
                kaist_total += 100

    return kaist_total

def _get_postech_total_score():
    postech_total = 0
    events_list = Event.objects.all()

    for event in events_list:
        if event.event_is_finished:
            if kaist_score < postech_score:
                postech_total += 100

    return postech_total
