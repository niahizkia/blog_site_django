from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog


def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs':blogs})

def single(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blogs/single.html', {'blog':blog})

def comment(request, id):
    blog = get_object_or_404(Blog, pk=id)

    if request.method == 'POST':
        newDesc = request.POST['desc']
        
        if len(newDesc) < 10:
            return render(request, 'blogs/single.html', {
                'blog':blog,
                'errors':'komentar min 10 karakter'
            })
        blog.comment_set.create(desc=newDesc)
        return render(request, 'blogs/single.html', {'blog':blog})