from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Blog
from . import forms


def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs':blogs})

def single(request, id):
    blog = get_object_or_404(Blog, pk=id)
    form = forms.CommentForm()
    return render(request, 'blogs/single.html', {'blog':blog, 'form':form})

def comment(request, id):
    blog = get_object_or_404(Blog, pk=id)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            newDesc = request.POST['desc']
            blog.comment_set.create(desc=newDesc)
            
            messages.success(request, 'Comment sent..')
            return HttpResponseRedirect(reverse('blogs:index'))
        # return render(request, 'blogs/single.html', {'blog':blog})