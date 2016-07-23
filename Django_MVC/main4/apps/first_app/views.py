from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.views.generic import DeleteView
# Create your views here.

def index(request):
    #This captures all from the blogs object below
    context = {
    "blogs" : Blog.objects.all()
    }
    #equivalent to query of select * from Blog
    return render(request, "first_app/index.html", context)

def blogs(request):
    #Using ORM here, go to that Class.managerofthatclass.create(variable1=request.POST['variable1'], variable2=request.POST['variable2'])
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now() )
    return redirect('/')

def comments(request, id):
    #Using ORM here, go to that Class.managerofthatclass.create(variable1=request.POST['variable1'], variable2=request.POST['variable2'])
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now() )
    return redirect('/')
