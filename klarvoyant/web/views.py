# Create your views here.

import os
import re
import os.path
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.db import models
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.utils import simplejson

from web.models import Contactus, Dates, Slideshow, Menu
from web.forms import ContactUsForm

def home(request):
    try:
        latest_content = Feature.objects.latest('id')
        latest_events = Newsevents.objects.latest('id')
        slideshow = Slideshow.objects.latest('id')
        context = { 
            'latest_content': latest_content,
            'latest_events': latest_events,
            'slideshow' : slideshow,
        }
    except:
        context = {}
    
    return render(request, 'home.html',context)
    
def rendermenu(request, menuslug):
    if menuslug:
        template = "%s.html" % menuslug
        aboutus = ''
        form = ''
        menu = Menu.objects.get(slug=menuslug)
        sub_menus = menu.submenu_set.all()
        if sub_menus.count():
            return rendersubmenu(request, menuslug, sub_menus[0].slug)
        
        if menuslug == 'about_us':            
            aboutus = Aboutus.objects.latest('id')
        elif menuslug == 'contact_us':
            form = ContactUsForm()
        context = {
            'aboutus': aboutus,
            'form': form,
        }
        return render(request, template, context)


def rendersubmenu(request, menu_slug, submenuslug):
    if menu_slug:
        if submenuslug:
            template = "%s.html" % submenuslug
            freshersform = ''
            vacancies = ''
            
            if submenuslug == 'freshers':
                freshersform = CandidateFreshersForm()

            elif submenuslug == 'experienced':
                vacancies = Vacancy.objects.all().exclude(name = 'Freshers')
            context = {
                'form': freshersform,
                'vacancies': vacancies,
            }
            return render(request, template, context)

class ContactUsView(View):

    def get(self,request):

        context = {}
        form = ''
        form = ContactUsForm()
        context = {
            'form': form,
        }
        return render(request,'contact_us.html', context)

    def post(self, request):

        form = ContactUsForm(request.POST)
        data_dict_form = request.POST
        context = {}
        if request.method == 'POST':
            if form.is_valid():
                contact_us = Contactus()
                contact_us.name = data_dict_form['name']
                contact_us.email_id = data_dict_form['email_id']
                contact_us.message = data_dict_form['message']
                contact_us.subject = data_dict_form['subject']
                contact_us.save();
                contact_us.send_contact_notification_mail_to_admins()
                form = ContactUsForm()
                context ={
                    'form': form,
                    'message': 'Your message sent successfully',
                }
            else:
                context ={
                    'form': form,
                }
        return render(request, 'contact_us.html', context)
        
