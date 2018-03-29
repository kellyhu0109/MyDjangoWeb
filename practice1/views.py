from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {
        'posts':posts,
    })

def show(request, num):
    # post = Post.objects.get(id=num)
    post = get_object_or_404(Post, id=num)
    return render(request, 'posts/show.html', {
        'post':post,
    })

def new():
    pass

def edit():
    pass

def delete():
    pass