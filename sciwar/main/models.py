# -*- coding: utf-8
from django.db import models
from django.contrib import admin

SCHOOLS = (
    (1, u'KAIST'),
    (2, u'POSTECH'),
)

class Building(models.Model):
    building_name = models.CharField(max_length=100,db_index=True)
    building_location_x = models.SmallIntegerField() # 지도상의 x,y
    building_location_y = models.SmallIntegerField()

class Player(models.Model):
    player_name = models.CharField(max_length=100,db_index=True)
    player_school = models.SmallIntegerField(choices=SCHOOLS)

class Video(models.Model):
    video_link = models.CharField(max_length=300,db_index=True)
    video_name = models.CharField(max_length=100)
    video_time = models.DateTimeField()

class Event(models.Model):
    event_id = models.IntegerField()
    event_name = models.CharField(max_length=100,db_index=True)
    event_time = models.DateTimeField()
    event_building = models.ForeignKey(Building,db_index=True)
    event_kaist_score = models.SmallIntegerField()
    event_postech_score = models.SmallIntegerField()
    event_kaist_players = models.ForeignKey(Player, related_name='KAIST', db_index=True)
    event_postech_players = models.ForeignKey(Player, related_name='POSTECH', db_index=True)
    event_videos = models.ForeignKey(Video, db_index=True) # 경기 끝난 후 올라가는 영상들

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'building_location_x', 'building_location_y')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'player_school')

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'event_time', 'event_building', 'event_kaist_score', 'event_postech_score', 'event_kaist_players', 'event_postech_players', 'event_videos')
