from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^process/(?P<which_process>\w+)$', views.process),
	url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    #url(r'^add$', views.add),
    url(r'^enroll/(?P<id>\d+)$', views.enroll),
    #url(r'^schedule/(?P<id>\d+)$', views.schedule),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)
]
