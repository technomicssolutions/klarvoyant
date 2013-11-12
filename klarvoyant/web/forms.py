from django import forms
from django.forms import ModelForm

from .models import Contactus

class ContactUsForm(ModelForm):

    class Meta:
        model = Contactus
        fields = ('name', 'email_id', 'mobile', 'subject' , 'message')
        

