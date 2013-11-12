from django.db import models
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, mail_managers, send_mail, EmailMessage, mail_admins
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from klarvoyant.utils import slug

class Dates(models.Model):
    created_date = models.DateTimeField('Created Date', auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField('Modified Date', auto_now=True, null=True, blank=True)

class Logo(Dates):
    logo = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as the logo in the page")

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'
            
    # def __unicode__(self):
    #     return self.

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.logo
    image_thumb.allow_tags = True
class Slideshow(Dates):
    left_arrow = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed in the banner" )
    right_arrow = models.ImageField(upload_to='uploads/images', help_text="Upload image to be displayed in the banner" )
    max_slide_count = models.IntegerField('Slide Count', help_text='Maximum number of slides to be appear in the banner', default=3)
    bullet_active = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as the active bullet in the banner" )
    bullet_inactive = models.ImageField(upload_to='uploads/images/', help_text="Upload image to be displayed as the inactive bullet in the banner" )
    class Meta:
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshow'
            

    def left_arrow_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.left_arrow
    left_arrow_thumb.allow_tags = True 

    def right_arrow_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.right_arrow
    right_arrow_thumb.allow_tags = True

    def bullet_active_thumb(self):
        return '<img height="19px" src="/site_media/%s"/>' % self.bullet_active
    bullet_active.allow_tags = True

    def bullet_inactive_thumb(self):
        return '<img height="19px" src="/site_media/%s"/>' % self.bullet_inactive
    bullet_inactive.allow_tags = True

class Slide(Dates):
    text = models.CharField('Slogan', max_length = 200, null=True, blank=True, help_text='Slogan to be displayed in the banner')
    image = models.ImageField(upload_to='uploads/images/', help_text='Upload image to be displayed as slideshow')
    slideshow_id = models.ForeignKey(Slideshow, help_text='Corresponding Slideshow image')
    
    class Meta:
        verbose_name = 'Slides'
        verbose_name_plural = 'Slides'

    def image_thumb(self):
        return '<img height="50px" src="/site_media/%s"/>' % self.image
    image_thumb.allow_tags = True 

class Menu(Dates):
    title = models.CharField('Menu', max_length = 50, help_text = 'Name of the menu')
    slug = models.CharField('Slug', max_length = 100, help_text = 'Slug of the menu')
    order = models.IntegerField('Order', max_length = 10, default = '1', help_text = 'Order of the menus')
    template = models.CharField('Template Name', max_length = 100, default = 'name of the template', help_text= 'Name of the Template')
    # banner_image = models.ImageField(upload_to='uploads/images/', help_text="Upload banner to be displayed in the corresponding page")
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def save(self, *args, **kwargs):
        self.slug = slug(self.title)
        super(Menu, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Submenu(Dates):
    menu = models.ForeignKey(Menu, help_text = 'Corresponding menu')
    title = models.CharField('Submenu', max_length = 200 , help_text = 'Name of the submenu')
    slug = models.CharField('Slug', max_length = 200, help_text = 'Slug of the submenu')
    order = models.IntegerField('Order', max_length = 10, default = '1', help_text = 'Order of the submenu')
    # banner_image = models.ImageField(upload_to='uploads/images/', help_text="Upload banner to be displayed in the corresponding page")

    def save(self, *args, **kwargs):
        self.slug = slug(self.title)
        super(Submenu, self).save(*args, **kwargs) 

    def __unicode__(self):
        return self.title                     
        
class Contactus(Dates):
    name = models.CharField('Name', max_length=80)
    email_id = models.EmailField('Email', max_length = 120)
    mobile = models.CharField('Mobile No', max_length = 50)
    subject = models.CharField('Subject', max_length = 100)
    message = models.TextField('Message')
    
    def __unicode__(self):
        return self.name

    def send_contact_notification_mail_to_admins(self):
        root_url = 'http://%s'%(Site.objects.get_current().domain)
        subject = self.subject
        # contact_us/subject = 'Contact me'. self.name
        message = render_to_string('email/contactus_notification.html', {
            'name': self.name,
            'email': self.email_id,
            'content': self.message,
            'subject': self.subject,
            'root_url': root_url,
        }) 
        try:
            mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
        except BadHeaderError:
            return HttpResponse('Invalid Header Found')

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
