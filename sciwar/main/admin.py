#-*-coding:utf-8-*-
from django.contrib import admin
from django.db import models 
from main.models import *


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('link','name','time','event')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'winner', 'score', 'start_time', 'end_time', 'building', 'kaist_score', 'postech_score')

class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'time')

class CheerMessageAdmin(admin.ModelAdmin):
    list_display = ('school','time','event','content')

class LiveUserAdmin(admin.ModelAdmin):
    list_display = ('token','last_access')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(CheerMessage, CheerMessageAdmin)
admin.site.register(LiveUser, LiveUserAdmin)
