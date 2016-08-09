from django.shortcuts import render, redirect, HttpResponse
from .models import User, UserManager
from django.contrib import messages
# Create your views here.

def index(request):
	# User.objects.all().delete()
	request.session.flush()
	return render(request, 'wall/index.html')

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
	    return render(request, 'wall/success.html', context)
    else:
	    return redirect('/')

def show(request, id):
    if 'status' in request.session:
        if request.method == 'GET':
            context = {
                'user' : User.objects.get(id=id)
                }
	    return render(request, 'wall/show.html', context)
    else:
	    return redirect('/success')

def edit(request, id):
    if 'status' in request.session:
	    if request.method == "GET":
		    context = {
			    'user': User.objects.get(id = id)
		        }
		    return render(request, 'wall/edit.html', context)
	    else: # if request is POST
    		val_result = User.userManager.edit(request.POST, id)
    		if val_result[0] == False:
    			for error in val_result[1]:
    				messages.error(request, error)
    			# return redirect(reverse('products_edit', id))
    			return redirect('/edit/{}'.format(id))
    		else: # if validation is OKAY (TRUE)
    			messages.success(request, val_result[1])
    			return redirect('/success')

def enroll(request, id):
    if 'status' in request.session:
	    if request.method == "GET":
                context = {
                'user': User.objects.get(id = id)
                }
		return render(request, 'wall/enroll.html', context)
	    else: # if request is POST
    		val_result = User.userManager.enroll(request.POST, id)
    		if val_result[0] == False:
    			for error in val_result[1]:
    				messages.error(request, error)
    			# return redirect(reverse('products_edit', id))
    			return redirect('/success')
    		else: # if validation is OKAY (TRUE)
    			messages.success(request, val_result[1])
    			return redirect('/show/{}'.format(id))

def destroy(request, id):
    if 'status' in request.session:
        if request.method == "GET":
            context = {
                'user': User.objects.get(id=id)
                }
            return render(request, 'wall/remove.html', context)
        elif request.method == "POST":
		        User.objects.get(id=id).delete()
		        return redirect('/success')
