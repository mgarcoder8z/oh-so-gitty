from django.conf.urls import url, include
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import admin

urlpatterns = [
    url(r'^/', include('apps.word_app.urls')),
]
