# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CheerMessage.event'
        db.add_column('main_cheermessage', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Event']),
                      keep_default=False)

        # Adding index on 'CheerMessage', fields ['time']
        db.create_index('main_cheermessage', ['time'])


    def backwards(self, orm):
        # Removing index on 'CheerMessage', fields ['time']
        db.delete_index('main_cheermessage', ['time'])

        # Deleting field 'CheerMessage.event'
        db.delete_column('main_cheermessage', 'event_id')


    models = {
        'main.cheermessage': {
            'Meta': {'object_name': 'CheerMessage'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['main.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.SmallIntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'})
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