from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home, name="home"),
    url(r'^contact_us/$',views.ContactUsView.as_view(), name = "contactus"),
    url(r'^(?P<menuslug>[-\w]+)/$', views.rendermenu, name = "render_menupage"),
    url(r'^(?P<menu_slug>[-\w]+)/(?P<submenuslug>[-\w]+)/$', views.rendersubmenu, name = "render_submenupage"),
    url(r'^contact_notification/$', TemplateView.as_view(template_name='contactus_notification.html')),
)
