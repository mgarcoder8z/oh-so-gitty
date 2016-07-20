from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from . import views

def index(request):
    return render(request,"time_app/index.html", current_time)

urlpatterns = [
    url(r'^$', views.index),
  ]
