from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from web.views import home, ContactUsView, rendermenu, rendersubmenu

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

	url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home, name="home"),
    url(r'^contact_us/$',ContactUsView.as_view(), name = "contactus"),
    url(r'^(?P<menuslug>[-\w]+)/$', rendermenu, name = "render_menupage"),
    url(r'^(?P<menu_slug>[-\w]+)/(?P<submenuslug>[-\w]+)/$', rendersubmenu, name = "render_submenupage"),
    url(r'^contact_notification/$', TemplateView.as_view(template_name='contactus_notification.html')),
)
