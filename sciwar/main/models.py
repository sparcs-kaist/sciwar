# -*- coding: utf-8
from django.db import models
from django.contrib import admin

SCHOOLS = (
    (1, u'KAIST'),
    (2, u'POSTECH'),
)

class Building(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    location_x = models.SmallIntegerField() # 지도상의 x,y
    location_y = models.SmallIntegerField()

class Player(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    school = models.SmallIntegerField(choices=SCHOOLS)

class Video(models.Model):
    link = models.CharField(max_length=300,db_index=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event = models.ForeignKey(Event, db_index=True) # 경기 끝난 후 올라가는 영상들

class Event(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    is_finished = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    building = models.ForeignKey(Building,db_index=True)
    kaist_score = models.SmallIntegerField()
    postech_score = models.SmallIntegerField()
    kaist_players = models.ManyToManyKey(Player, related_name='KAIST', null=True, db_index=True)
    postech_players = models.ManyToManyKey(Player, related_name='POSTECH', null=True, db_index=True)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_x', 'location_y')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('link','name','time','event')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_finished', 'start_time', 'end_time', 'building', 'kaist_score', 'postech_score')

admin.site.register(Building, BuildingAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Event, EventAdmin)
