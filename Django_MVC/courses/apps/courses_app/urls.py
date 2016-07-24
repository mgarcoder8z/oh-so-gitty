from django.conf.urls import url, include
from . import views
import re

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/comment/(?P<id>\d+)$', views.comment)
]
