# -*- coding: utf-8
from django.db import models
from django.contrib import admin

SCHOOLS = (
    (1, u'KAIST'),
    (2, u'POSTECH'),
    (3, u'NONE'),
)

NOTIFY = (
        (1, u'NOTICE'),
        (2, u'INFOMATION'),
)

class Player(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    school = models.SmallIntegerField(choices=SCHOOLS)


class Event(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    winner = models.SmallIntegerField(choices=SCHOOLS)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    building = models.CharField(max_length=50)
    kaist_score = models.SmallIntegerField()
    postech_score = models.SmallIntegerField()
    score = models.SmallIntegerField()
    kaist_players = models.ManyToManyField(Player, related_name='KAIST', blank=True, db_index=True)
    postech_players = models.ManyToManyField(Player, related_name='POSTECH', blank=True, db_index=True)

class Video(models.Model):
    link = models.CharField(max_length=300,db_index=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event = models.ForeignKey(Event, db_index=True) # 경기 끝난 후 올라가는 영상들

class Infor(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.SmallIntegerField(choices=NOTIFY)
    time = models.DateTimeField()

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('link','name','time','event')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'winner', 'score', 'start_time', 'end_time', 'building', 'kaist_score', 'postech_score')

class InforAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'time')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Infor, InforAdmin)
