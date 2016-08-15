from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
    def register(self, info):
    	first_name = str(info['first_name'])
    	last_name = str(info['last_name'])
    	email = info['email']
    	password = info['password']
    	confirm = info['confirm']
    	errors = []
    	if len(first_name) < 2:
    		errors.append('First name is too short!')
    	elif str.isalpha(first_name) != True:
    		errors.append('First name should only contain alphabets!')
    	if len(last_name) < 2:
    		errors.append('Last name is too short!')
    	elif str.isalpha(last_name) != True:
    		errors.append('Last name should only contain alphabets!')
    	if len(email) < 1:
    		errors.append('Email cannot be blank!')
    		# if email doesn't match regular expression,
    		# display an invlaid email address message.
    	elif not EMAIL_REGEX.match(email):
    		errors.append('Invalid Email Address!')
    	try:
    		if User.objects.get(email=email):
    			errors.append('Same email already exist!')
    	except:
    		pass
    	if len(password) < 8:
    		errors.append('Password should be longer than 8 characters!')
    	elif password != confirm:
    		errors.append('Your password does not match the confirmed password!')

    	if errors:
    		return (False, errors)
    	else:
    		hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    		User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed)
    		return (True, 'Successfully registered!')

    def login(self, info):
    	errors = []
    	email = info['email']
    	password = info['password']
    	try:
    		user = User.objects.get(email=email)
    		if bcrypt.hashpw(password.encode(), user.password.encode()) != user.password:
    			errors.append('Your password is probably wrong.')
    	except:
    		errors.append('Not existing email. Please register!')
        if errors:
            return (False, errors)
        else:
            return (True, 'Successfully logged in!', user.id)

    def success(self, id):
        if request.method =='GET':
            context = {
                'users' : User.objects.all()
            }
        return render(request, 'mybootstrap/index.html', context)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    house = models.CharField(max_length=45)
    first_course = models.CharField(max_length=100)
    second_course = models.CharField(max_length=100)
    third_course = models.CharField(max_length=100)
    password = models.CharField(max_length=255) # hashed password
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	# *************************
	# Connect an instance of UserManager to our User model!
    userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
    objects = models.Manager()
	# *************************
