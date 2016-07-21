from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^result$', views.result),
  ]
