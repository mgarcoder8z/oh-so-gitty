from __future__ import unicode_literals
from django.db import models

# Create your models here. Make sure to use Capitals for model and singular
class Course(models.Model):
	course_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
	description = models.TextField(max_length=500)
    #To define a one-to-one relationship, use OneToOneField.
	course = models.OneToOneField(
		Course,
		on_delete=models.CASCADE,#this will delete the entire object including the description, date and time
		primary_key=True,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	course = models.ForeignKey(Course)#This is the foreign key forming the many to one connection to Course
	comment = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
