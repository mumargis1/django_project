from django.shortcuts import render
from django.http import HttpResponse
from sympy import content
from .models import Post

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home </h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1> Blog About </h1>')
    return render(request, 'blog/about.html', {'title':': About'})
