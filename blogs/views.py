from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs':blogs})


def single(request, id):
    blog = Blog.objects.get(pk = id)
    return render(request, 'blogs/single.html', {'blog':blog})