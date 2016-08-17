from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def register(self, info):
		name = str(info['name'])
		alias = str(info['alias'])
		email = info['email']
		password = info['password']
		confirm_pw = info['confirm_pw']
		errors = []
		if len(name) < 2:
			errors.append('Your name is too short! Must be more than 2 characters!')
		elif len(name) > 100:
			errors.append('Your name is too long! Must be less than 100 characters!')
		elif str.isalpha(str(info['name'].replace(' ', ''))) != True:
			errors.append('Your name should only contain letters!')
		if len(alias) < 2:
			errors.append('Your alias is too short! Must be more than 2 characters!')
		elif len(alias) > 100:
			errors.append('You alias is too long! Must be less than 100 characters!')
		elif str.isalpha(alias) != True:
			errors.append('Your alias should only contain letters! No spaces or symbols')
		if len(email) < 1:
			errors.append('Email cannot be blank!')
			# if email doesn't match regular expression,
			# display an invlaid email address message.
		elif not EMAIL_REGEX.match(email):
			errors.append('Invalid Email Address!')
		try:
			if User.objects.get(email=email):
				errors.append('Same email already exists!')
		except:
			pass
		if len(password) < 8:
			errors.append('Password must be longer than 8 characters!')
		elif password != confirm_pw:
			errors.append('Your password does not match the confirmed password!')

		if errors:
			return (False, errors)
		else:
			hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			User.objects.create(name = name, alias = alias, email = email, hashed_pw = hashed_pw)
			return (True, 'Successfully registered!')

	def login(self, info):
		errors = []
		email = info['email']
		password = info['password']
		try:
			user = User.objects.get(email=email)
			if bcrypt.hashpw(password.encode(), user.hashed_pw.encode()) != user.hashed_pw:
				errors.append('Your password is incorrect, please check and try again.')
		except:
			errors.append('Not existing email. Please register!')

		if errors:
			return (False, errors)
		else:
			return (True, 'Successfully logged in!' , user.alias, user.id)

	def user_info(self, user_id):
		basic = User.objects.get(id=user_id)

		total_review = Review.objects.raw("SELECT book_review.id, COUNT(book_review.user_id) AS 'count_review' FROM book_review WHERE book_review.user_id = {} GROUP BY book_review.user_id".format(user_id))
		count_review = total_review[0].count_review

		review_list = Review.objects.raw("SELECT book_review.id, book_review.book_id, book_book.title FROM book_review JOIN book_book ON book_review.book_id = book_book.id WHERE book_review.user_id = {}".format(user_id))

		return (basic, count_review, review_list)
class reviewManager(models.Manager):
	def add_review(self, check_info, book_id, user_id):
		description = str(check_info['description'])
		rating = int(check_info['rating'])
		errors = []
		if len(description) < 30:
			errors.append('Please add review more than 30 characters long!')
		elif len(description) > 500:
			errors.append('Please keep your review under 500 characters!')

		if errors:
			return (False, errors)
		else:
			Review.objects.create(description = description, rating = rating, user_id = user_id, book_id = book_id)
			return (True, 'Successfully added a new book with your review!')

class bookManager(models.Manager):
	def new_book(self, book_info, user_id):

		title = str(book_info['title'])
		if len(str(book_info['author_new'])) > 1:
			author = str(book_info['author_new'])
		else:
			author = str(book_info['author_list'])
		author_temp = author
		description = str(book_info['description'])
		rating = int(book_info['rating'])

		errors = []

		if len(title) < 1:
			errors.append('Please add the title of the book!')
		elif len(title) > 200:
			errors.append('Please keep the title of the book fewer than 200 characters!')
		try:
			if Book.objects.get(title=title):
				errors.append('Same title already exist!')
		except:
			pass
		if len(author) < 1:
			errors.append('Please add the author of the book!')
		elif len(author) > 100:
			errors.append('Please keep the name of the author fewer than 100 characters!')
		elif str.isalpha(str(author_temp.replace(' ', ''))) != True:
			errors.append('Name of the author cannot contain numbers or symbols!')
		if len(description) < 30:
			errors.append('Please add review more than 30 characters long!')
		elif len(description) > 500:
			errors.append('Please keep your review under 500 characters!')

		if errors:
			return (False, errors)
		else:
			Book.objects.create(title = title, author = author)
			book = Book.objects.get(title = title, author = author)
			Review.objects.create(description = description, rating = rating, book_id = book.id, user_id = user_id)
			return (True, 'Successfully added a new book with your review!', book.id)
	def getting_info(self, book_id):
		book_data = Book.objects.raw("SELECT book_book.id, book_book.title, book_book.author, book_review.description, book_review.rating, book_review.id AS 'review_id', book_user.id AS 'user_id', book_user.alias, book_review.created_at AS 'created_at' FROM book_book JOIN book_review ON book_book.id = book_review.book_id JOIN book_user ON book_user.id = book_review.user_id WHERE book_book.id = {} ORDER BY book_review.created_at ASC".format(book_id))
		return book_data
	def home_data(self):
		recent_review = Book.objects.raw("SELECT book_book.id, book_review.rating, book_user.id AS 'user_id', book_user.alias, book_review.description, book_review.created_at AS 'created_at' FROM book_book JOIN book_review ON book_review.book_id = book_book.id JOIN book_user ON book_review.user_id = book_user.id ORDER BY book_review.created_at DESC LIMIT 3")
		books = Book.objects.all()
		return (recent_review, books)


class User(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	email = models.EmailField()
	hashed_pw = models.CharField(max_length=255) # hashed password
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
	# *************************

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	bookManager = bookManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()

class Review(models.Model):
	rating = models.IntegerField()
	description = models.TextField(max_length=500)
	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	reviewManager = reviewManager()
	# Re-adds objects as a manager (so all the normal ORM literature matches)
	objects = models.Manager()
