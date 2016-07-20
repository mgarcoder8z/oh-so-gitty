from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^word_generator$', views.word_generator),
    url(r'^reset$', views.reset),
  ]
