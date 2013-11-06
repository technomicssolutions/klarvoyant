from django.contrib import admin
from django.db import models
from models import Dates, Logo, Slideshow, Slide, Menu, Submenu, Contactus
from adminthumnail import AdminImageWidget
from django.views.generic.list import ListView

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_id', 'subject', 'message')

class SlideInline(admin.TabularInline):
    model = Slide
    initial_forms = 3
    max_num = 3
    extra = 0

    fk_name = 'slideshow_id'
    list_display = ('text', 'image_thumb')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class SlideshowAdmin(admin.ModelAdmin):
    inlines = [SlideInline]
    list_display = ('right_arrow_thumb', 'left_arrow_thumb', 'max_slide_count','bullet_active_thumb', 'bullet_inactive_thumb')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

class SubmenuInline(admin.TabularInline):
    model = Submenu

    fk_name = 'menu'
    list_display = ('sub_title', 'slug', 'order')
    exclude = ('slug',)

class MenuAdmin(admin.ModelAdmin):
    inlines = [SubmenuInline]
    list_display = ('title', 'slug', 'order')
    exclude = ('slug',)

class LogoAdmin(admin.ModelAdmin):
    list_display = ['logo']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget()},
    }

admin.site.register(Slideshow, SlideshowAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Contactus, ContactusAdmin)
admin.site.register(Logo, LogoAdmin)

