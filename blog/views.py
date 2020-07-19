from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog  
# Create your views here.


def home(request):
    return render(request, 'index.html')


def blogs(request):
    blogs = Blog.objects.all()
    print(blogs)
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog.html', context)
