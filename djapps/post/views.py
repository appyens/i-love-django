from django.shortcuts import render
from .models import Post, Comment

# Create your views here.


def home(request):
    latest_posts = Post.objects.filter(status='draft')[:5]
    return render(request, 'post/home.html', {'posts': latest_posts})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

