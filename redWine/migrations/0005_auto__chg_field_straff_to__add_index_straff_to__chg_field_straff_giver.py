# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Straff.to' to match new field type.
        db.rename_column(u'redWine_straff', 'to', 'to_id')
        # Changing field 'Straff.to'
        db.alter_column(u'redWine_straff', 'to_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redWine.Bruker']))
        # Adding index on 'Straff', fields ['to']
        db.create_index(u'redWine_straff', ['to_id'])


        # Renaming column for 'Straff.giver' to match new field type.
        db.rename_column(u'redWine_straff', 'giver', 'giver_id')
        # Changing field 'Straff.giver'
        db.alter_column(u'redWine_straff', 'giver_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redWine.Bruker']))
        # Adding index on 'Straff', fields ['giver']
        db.create_index(u'redWine_straff', ['giver_id'])


    def backwards(self, orm):
        # Removing index on 'Straff', fields ['giver']
        db.delete_index(u'redWine_straff', ['giver_id'])

        # Removing index on 'Straff', fields ['to']
        db.delete_index(u'redWine_straff', ['to_id'])


        # Renaming column for 'Straff.to' to match new field type.
        db.rename_column(u'redWine_straff', 'to_id', 'to')
        # Changing field 'Straff.to'
        db.alter_column(u'redWine_straff', 'to', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Renaming column for 'Straff.giver' to match new field type.
        db.rename_column(u'redWine_straff', 'giver_id', 'giver')
        # Changing field 'Straff.giver'
        db.alter_column(u'redWine_straff', 'giver', self.gf('django.db.models.fields.CharField')(max_length=30))

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
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'straffer_gitt'", 'to': u"orm['redWine.Bruker']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'straffer'", 'to': u"orm['redWine.Bruker']"})
        }
    }

    complete_apps = ['redWine']