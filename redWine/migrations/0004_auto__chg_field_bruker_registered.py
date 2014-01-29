# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Bruker.registered'
        db.alter_column(u'redWine_bruker', 'registered', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):

        # Changing field 'Bruker.registered'
        db.alter_column(u'redWine_bruker', 'registered', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'redWine.bruker': {
            'Meta': {'object_name': 'Bruker'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'komite': ('django.db.models.fields.CharField', [], {'default': "'dotKom'", 'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'registered': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'totalWines': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'redWine.straff': {
            'Meta': {'object_name': 'Straff'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'giver': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'to': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['redWine']