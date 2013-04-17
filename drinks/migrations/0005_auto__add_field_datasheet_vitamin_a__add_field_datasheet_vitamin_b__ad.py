# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DataSheet.vitamin_a'
        db.add_column(u'drinks_datasheet', 'vitamin_a',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b'
        db.add_column(u'drinks_datasheet', 'vitamin_b',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_d'
        db.add_column(u'drinks_datasheet', 'vitamin_d',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b2'
        db.add_column(u'drinks_datasheet', 'vitamin_b2',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_e'
        db.add_column(u'drinks_datasheet', 'vitamin_e',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b12'
        db.add_column(u'drinks_datasheet', 'vitamin_b12',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_k'
        db.add_column(u'drinks_datasheet', 'vitamin_k',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b5'
        db.add_column(u'drinks_datasheet', 'vitamin_b5',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b7'
        db.add_column(u'drinks_datasheet', 'vitamin_b7',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b6'
        db.add_column(u'drinks_datasheet', 'vitamin_b6',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b3'
        db.add_column(u'drinks_datasheet', 'vitamin_b3',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.vitamin_b9'
        db.add_column(u'drinks_datasheet', 'vitamin_b9',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.calories'
        db.add_column(u'drinks_datasheet', 'calories',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.proteins'
        db.add_column(u'drinks_datasheet', 'proteins',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.sugar'
        db.add_column(u'drinks_datasheet', 'sugar',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'DataSheet.fat'
        db.add_column(u'drinks_datasheet', 'fat',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DataSheet.carbohydrate'
        db.add_column(u'drinks_datasheet', 'carbohydrate',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DataSheet.vitamin_a'
        db.delete_column(u'drinks_datasheet', 'vitamin_a')

        # Deleting field 'DataSheet.vitamin_b'
        db.delete_column(u'drinks_datasheet', 'vitamin_b')

        # Deleting field 'DataSheet.vitamin_d'
        db.delete_column(u'drinks_datasheet', 'vitamin_d')

        # Deleting field 'DataSheet.vitamin_b2'
        db.delete_column(u'drinks_datasheet', 'vitamin_b2')

        # Deleting field 'DataSheet.vitamin_e'
        db.delete_column(u'drinks_datasheet', 'vitamin_e')

        # Deleting field 'DataSheet.vitamin_b12'
        db.delete_column(u'drinks_datasheet', 'vitamin_b12')

        # Deleting field 'DataSheet.vitamin_k'
        db.delete_column(u'drinks_datasheet', 'vitamin_k')

        # Deleting field 'DataSheet.vitamin_b5'
        db.delete_column(u'drinks_datasheet', 'vitamin_b5')

        # Deleting field 'DataSheet.vitamin_b7'
        db.delete_column(u'drinks_datasheet', 'vitamin_b7')

        # Deleting field 'DataSheet.vitamin_b6'
        db.delete_column(u'drinks_datasheet', 'vitamin_b6')

        # Deleting field 'DataSheet.vitamin_b3'
        db.delete_column(u'drinks_datasheet', 'vitamin_b3')

        # Deleting field 'DataSheet.vitamin_b9'
        db.delete_column(u'drinks_datasheet', 'vitamin_b9')

        # Deleting field 'DataSheet.calories'
        db.delete_column(u'drinks_datasheet', 'calories')

        # Deleting field 'DataSheet.proteins'
        db.delete_column(u'drinks_datasheet', 'proteins')

        # Deleting field 'DataSheet.sugar'
        db.delete_column(u'drinks_datasheet', 'sugar')

        # Deleting field 'DataSheet.fat'
        db.delete_column(u'drinks_datasheet', 'fat')

        # Deleting field 'DataSheet.carbohydrate'
        db.delete_column(u'drinks_datasheet', 'carbohydrate')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'drinks.dailydrink': {
            'Meta': {'object_name': 'DailyDrink'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drinks.Profile']"}),
            'volume': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'drinks.datasheet': {
            'Meta': {'object_name': 'DataSheet'},
            'calories': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'carbohydrate': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'fat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proteins': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'sugar': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_a': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b12': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b2': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b3': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b5': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b6': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b7': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_b9': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_c': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_d': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_e': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'vitamin_k': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'drinks.drink': {
            'Meta': {'object_name': 'Drink'},
            'caffeine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'datasheet': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['drinks.DataSheet']", 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'unknown drink'", 'max_length': '128'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'drinks.drinkstats': {
            'Meta': {'object_name': 'DrinkStats'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'drink': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drinks.Drink']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['drinks.Profile']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'drinks.profile': {
            'Meta': {'object_name': 'Profile'},
            'drinks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['drinks.Drink']", 'through': u"orm['drinks.DrinkStats']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['drinks']