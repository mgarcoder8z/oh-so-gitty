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
        house = info['house']
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
    		User.objects.create(first_name = first_name, last_name = last_name, email = email, house = house, password = hashed)
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

    def show(self, id):
        if request.method =='GET':
            context = {
                'user' : User.objects.get(id=id)
            }
        return render(request, 'wall/show.html', context)

    def success(self, id):
        if request.method =='GET':
            context = {
                'users' : User.objects.all()
            }
        return render(request, 'wall/success.html', context)

    def edit(self, data, user_id):
        first_name = str(data['first_name'])
        last_name = str(data['last_name'])
        email = data['email']
        house = data['house']
        first_course = data['first_course']
        second_course = data['second_course']
        third_course = data['third_course']
        user = User.objects.get(id=user_id) # variable to get individual parts of object to edit
        errors = []
        if len(first_name) < 2:
            errors.append('First Name must contain more than 2 characters')
        elif str.isalpha(first_name) != True:
            errors.append('First name should only contain letters!')
        #Check if last name is alpha characters only and not blank
        if len(last_name) < 2:
            errors.append('Last Name must contain more than 2 characters')
        elif str.isalpha(last_name) != True:
            errors.append('First name should only contain letters!')
        if len(house) < 1:
            errors.append('House is required, choose Not Assigned, if unknown')
        #Check if email is valid format and not blank
        if len(email) < 1:
    		errors.append('Email cannot be blank!')
    		# if email doesn't match regular expression,
    		# display an invlaid email address message.
        elif not EMAIL_REGEX.match(email):
            errors.append('Invalid Email Address Format')
        if len('first_course') < 1:
            errors.append('Must select a first course')
        if len('second_course') < 1:
            errors.append('Must select a second course')
        if len('third_course') < 1:
            errors.append('Must select a third course')
        try:
            user = User.objects.get(first_course=first_course)
            errors.append('User Already Registered')
        except:
            pass
        if errors:
    		return (False, errors)
        else:
            #hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.house = house
            user.first_course = first_course
            user.second_course = second_course
            user.third_course = third_course
            user.save()
            #User.objects.update(first_name = first_name, last_name = last_name, email = email, house = house)
            return (True, 'Successfully updated!')

    def enroll(self, info, user_id):
        first_course = info['first_course']
        second_course = info['second_course']
        third_course = info['third_course']
        errors = []
        user = User.objects.get(id=user_id)
        if len('first_course') < 1:
            errors.append('Must select a first course')
        if len('second_course') < 1:
            errors.append('Must select a second course')
        if len('third_course') < 1:
            errors.append('Must select a third course')
        #try:
            #user = User.objects.get(first_course=first_course)
            #errors.append('User Already Registered')
        #except:
            #pass
        if errors:
            return (False, errors)
        else:
            user.first_course = first_course
            user.second_course = second_course
            user.third_course = third_course
            user.save()
            return (True, 'Successfully Enrolled', user.id)


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
