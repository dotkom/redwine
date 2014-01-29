# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bruker'
        db.create_table(u'redWine_bruker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('totalWines', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('registered', self.gf('django.db.models.fields.DateTimeField')()),
            ('komite', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'redWine', ['Bruker'])

        # Adding model 'Straff'
        db.create_table(u'redWine_straff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('giver', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'redWine', ['Straff'])


    def backwards(self, orm):
        # Deleting model 'Bruker'
        db.delete_table(u'redWine_bruker')

        # Deleting model 'Straff'
        db.delete_table(u'redWine_straff')


    models = {
        u'redWine.bruker': {
            'Meta': {'object_name': 'Bruker'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'komite': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'registered': ('django.db.models.fields.DateTimeField', [], {}),
            'totalWines': ('django.db.models.fields.PositiveIntegerField', [], {})
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