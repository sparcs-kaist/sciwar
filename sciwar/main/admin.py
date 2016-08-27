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

class BoardContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ['title', 'content']

class TotoContentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'score1_1', 'score1_2', 'score2_1', 'score2_2', 'score3_1', 'score3_2', 'score4_1', 'score4_2', 'winner1', 'winner2', 'winner3', 'winner4', 'winner5', 'winner6', 'winner7')
    search_fields = ['student_id', 'name']


admin.site.register(Player, PlayerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(CheerMessage, CheerMessageAdmin)
admin.site.register(LiveUser, LiveUserAdmin)
admin.site.register(BoardContent, BoardContentAdmin)
admin.site.register(TotoContent, TotoContentAdmin)
