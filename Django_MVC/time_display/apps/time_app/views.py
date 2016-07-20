from django.shortcuts import render, HttpResponse
from time import strftime, localtime
  
def index(request):
	current_time = { 'time': strftime('%b %d, %Y %I:%M %p', localtime()) }
	return render(request, 'time_app/index.html', current_time)
