# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('main_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('school', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('main', ['Player'])

        # Adding model 'Event'
        db.create_table('main_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('winner', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('is_competition', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('kaist_score', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('postech_score', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('score', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('main', ['Event'])

        # Adding M2M table for field kaist_players on 'Event'
        m2m_table_name = db.shorten_name('main_event_kaist_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['main.event'], null=False)),
            ('player', models.ForeignKey(orm['main.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'player_id'])

        # Adding M2M table for field postech_players on 'Event'
        m2m_table_name = db.shorten_name('main_event_postech_players')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['main.event'], null=False)),
            ('player', models.ForeignKey(orm['main.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'player_id'])

        # Adding model 'Video'
        db.create_table('main_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=300, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Event'])),
        ))
        db.send_create_signal('main', ['Video'])

        # Adding model 'Info'
        db.create_table('main_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('main', ['Info'])

        # Adding model 'CheerMessage'
        db.create_table('main_cheermessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('school', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('main', ['CheerMessage'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('main_player')

        # Deleting model 'Event'
        db.delete_table('main_event')

        # Removing M2M table for field kaist_players on 'Event'
        db.delete_table(db.shorten_name('main_event_kaist_players'))

        # Removing M2M table for field postech_players on 'Event'
        db.delete_table(db.shorten_name('main_event_postech_players'))

        # Deleting model 'Video'
        db.delete_table('main_video')

        # Deleting model 'Info'
        db.delete_table('main_info')

        # Deleting model 'CheerMessage'
        db.delete_table('main_cheermessage')


    models = {
        'main.cheermessage': {
            'Meta': {'object_name': 'CheerMessage'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.SmallIntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'main.event': {
            'Meta': {'object_name': 'Event'},
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_competition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kaist_players': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'KAIST'", 'blank': 'True', 'db_index': 'True', 'to': "orm['main.Player']"}),
            'kaist_score': ('django.db.models.fields.SmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'postech_players': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'POSTECH'", 'blank': 'True', 'db_index': 'True', 'to': "orm['main.Player']"}),
            'postech_score': ('django.db.models.fields.SmallIntegerField', [], {}),
            'score': ('django.db.models.fields.SmallIntegerField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'winner': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'main.info': {
            'Meta': {'object_name': 'Info'},
            'category': ('django.db.models.fields.SmallIntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'school': ('django.db.models.fields.SmallIntegerField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'main.video': {
            'Meta': {'object_name': 'Video'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['main']