from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Email, UserManager

# Create your views here.
def index(request):
    return render(request, 'email_val/index.html')

def process(request):
	if request.method == "POST":
		val_result = Email.userManager.email(request.POST['email'])
		if val_result[0] == False:
			request.session['error'] = val_result[1]
			return redirect('/')
		elif val_result[0] == True:
			Email.objects.create(email=request.POST['email'])
			request.session['message'] = val_result[1]
			return redirect('/success')
	else:
		return redirect('/')

def success(request):
	if request.method == "GET":
		context = {
			'emails': Email.objects.all()
		}
		return render(request, 'email_val/success.html', context)
	else: # If POST reset!
		try:
			del request.session['error']
			del request.session['message']
		except:
			pass
		return redirect('/')

def destroy(request, id):
	if request.method == "POST":
		email = Email.objects.get(id=id)
		request.session['message'] = "You have successfully deleted {}!".format(email.email)
		email.delete()
		return redirect('/success')
	else:
		return redirect('/success')
