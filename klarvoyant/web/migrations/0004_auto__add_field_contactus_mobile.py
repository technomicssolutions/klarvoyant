# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contactus.mobile'
        db.add_column(u'web_contactus', 'mobile',
                      self.gf('django.db.models.fields.CharField')(default='1234567890', max_length=50),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Contactus.mobile'
        db.delete_column(u'web_contactus', 'mobile')

    models = {
        u'web.contactus': {
            'Meta': {'object_name': 'Contactus', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '120'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'web.dates': {
            'Meta': {'object_name': 'Dates'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'web.logo': {
            'Meta': {'object_name': 'Logo', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.menu': {
            'Meta': {'object_name': 'Menu', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '10'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'name of the template'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.slide': {
            'Meta': {'object_name': 'Slide', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slideshow_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Slideshow']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'web.slideshow': {
            'Meta': {'object_name': 'Slideshow', '_ormbases': [u'web.Dates']},
            'bullet_active': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'bullet_inactive': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'left_arrow': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'max_slide_count': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'right_arrow': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.submenu': {
            'Meta': {'object_name': 'Submenu', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '10'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['web']