from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager
from django.contrib import messages
# Create your views here.

def main(request):
    request.session.flush()
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'mybootstrap/index.html', context)

def process(request, which_process):
	if request.method == "POST":
		if which_process == "register":
			val_result = User.userManager.register(request.POST)
			if val_result[0] == False: # aka registration info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/')
			else: # registration info is VALID (therefore, Successfully registered!)
				messages.success(request, val_result[1])
				request.session['name'] = request.POST['first_name']
				request.session['status'] = True
				return redirect('/success')
		else: # case when 'which_process' == "login"
			val_result = User.userManager.login(request.POST)
			if val_result[0] == False: # aka login info is INVALID
				for error in val_result[1]:
					messages.error(request, error)
				return redirect('/')
			else: # login info is VALID (therefore, Successfully logged in!)
				messages.success(request, val_result[1])
				request.session['user_id'] = val_result[2]
				request.session['status'] = True
                return redirect('/success')
	else:
            return redirect('/')

def logout(request):
	if 'status' in request.session:
		request.session.flush()
		messages.success(request, "Successfully logged off!")
		return redirect('/')
	else:
		messages.error(request, 'You must be logged in to go to that route!')
		return redirect('/')

def success(request):
    if 'status' in request.session:
        if request.method == 'GET':
            context = {
                'users' : User.objects.all()
                }
	    return render(request,'mybootstrap/index.html', context)
    else:
	    return redirect('/')
