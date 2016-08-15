from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
url(r'^$', views.main, name='main'),
url(r'^process/(?P<which_process>\w+)$', views.process),
url(r'^success/$', views.success),
url(r'^logout$', views.logout),
]
