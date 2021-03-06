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
        (2, u'INFO'),
)

class Player(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    school = models.SmallIntegerField(choices=SCHOOLS)
    year = models.CharField(max_length=10, blank=True)
    backnumber = models.IntegerField(null=True)
    position = models.CharField(max_length=40, blank=True)
    def __unicode__(self):
        return u'%s'%self.name

class Event(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    winner = models.SmallIntegerField(choices=SCHOOLS)
    is_competition = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    building = models.CharField(max_length=50)
    kaist_score = models.SmallIntegerField()
    postech_score = models.SmallIntegerField()
    score = models.SmallIntegerField()
    kaist_players = models.ManyToManyField(Player, related_name='KAIST', blank=True, db_index=True)
    postech_players = models.ManyToManyField(Player, related_name='POSTECH', blank=True, db_index=True)
    description = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Video(models.Model):
    link = models.CharField(max_length=300,db_index=True)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event = models.ForeignKey(Event, db_index=True) # 경기 끝난 후 올라가는 영상들

    def __unicode__(self):
        return u'%s : %s' % (self.event.name, self.name)

class Info(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.SmallIntegerField(choices=NOTIFY)
    time = models.DateTimeField()

    def __unicode__(self):
        return u'%s : %s' % (self.get_category_display(),self.title)

class CheerMessage(models.Model):
    content = models.CharField(max_length=140)
    school = models.SmallIntegerField(choices=SCHOOLS)
    time = models.DateTimeField(auto_now_add=True,db_index=True)
    event = models.ForeignKey(Event,default=1, db_index=True)

    def __unicode__(self):
        return u'<%s> %s' % (self.get_school_display(),self.event.name)

class LiveUser(models.Model):
    token = models.CharField(max_length=100,unique=True)
    last_access = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'<%s> %s'%(self.token,self.last_access)

class BoardContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s : %s' % (self.title, self.content)

class TotoContent(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    score1_1 = models.SmallIntegerField()
    score1_2 = models.SmallIntegerField()
    score2_1 = models.SmallIntegerField()
    score2_2 = models.SmallIntegerField()
    score3_1 = models.SmallIntegerField()
    score3_2 = models.SmallIntegerField()
    score4_1 = models.SmallIntegerField()
    score4_2 = models.SmallIntegerField()
    winner1 = models.SmallIntegerField(choices=SCHOOLS)
    winner2 = models.SmallIntegerField(choices=SCHOOLS)
    winner3 = models.SmallIntegerField(choices=SCHOOLS)
    winner4 = models.SmallIntegerField(choices=SCHOOLS)
    winner5 = models.SmallIntegerField(choices=SCHOOLS)
    winner6 = models.SmallIntegerField(choices=SCHOOLS)
    winner7 = models.SmallIntegerField(choices=SCHOOLS)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.name)
