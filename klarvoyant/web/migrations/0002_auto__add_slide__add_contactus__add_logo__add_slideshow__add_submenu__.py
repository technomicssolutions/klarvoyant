# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'web_slide', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slideshow_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Slideshow'])),
        ))
        db.send_create_signal(u'web', ['Slide'])

        # Adding model 'Contactus'
        db.create_table(u'web_contactus', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=120)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web', ['Contactus'])

        # Adding model 'Logo'
        db.create_table(u'web_logo', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'web', ['Logo'])

        # Adding model 'Slideshow'
        db.create_table(u'web_slideshow', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('left_arrow', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('right_arrow', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('max_slide_count', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('bullet_active', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('bullet_inactive', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'web', ['Slideshow'])

        # Adding model 'Submenu'
        db.create_table(u'web_submenu', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Menu'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default='1', max_length=10)),
        ))
        db.send_create_signal(u'web', ['Submenu'])

        # Adding model 'Dates'
        db.create_table(u'web_dates', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Dates'])

        # Adding model 'Menu'
        db.create_table(u'web_menu', (
            (u'dates_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.Dates'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='title', max_length=50)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='title', max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default='1', max_length=10)),
        ))
        db.send_create_signal(u'web', ['Menu'])

    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'web_slide')

        # Deleting model 'Contactus'
        db.delete_table(u'web_contactus')

        # Deleting model 'Logo'
        db.delete_table(u'web_logo')

        # Deleting model 'Slideshow'
        db.delete_table(u'web_slideshow')

        # Deleting model 'Submenu'
        db.delete_table(u'web_submenu')

        # Deleting model 'Dates'
        db.delete_table(u'web_dates')

        # Deleting model 'Menu'
        db.delete_table(u'web_menu')

    models = {
        u'web.contactus': {
            'Meta': {'object_name': 'Contactus', '_ormbases': [u'web.Dates']},
            u'dates_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.Dates']", 'unique': 'True', 'primary_key': 'True'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '120'}),
            'message': ('django.db.models.fields.TextField', [], {}),
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
            'slug': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'title'", 'max_length': '50'})
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