from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.db import models
from django.contrib import messages
import re
EMAIL = re.compile ('[a-zA-Z0-9\._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
# Create your models here.
#The usermanager below will process the validation of the email entered by user and
#return a result that can then be referenced in views.py

class UserManager(models.Manager):
    def email(self, email):
        if len(email) < 1:
            return(False, 'ERROR: Email Cannot Be Blank')
			# check if email doesn't match regular expression,
        elif not EMAIL.match(email):
            return(False, 'ERROR: Invalid email format')
        else:
			return(True, 'The email address you entered {} is a VALID email address! Thank you!'.format(email))

class Email(models.Model):
        email = models.EmailField(max_length=100)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

    	# This will connect the userManager to the email model
    	userManager = UserManager()
    	# ORM
    	objects = models.Manager()
