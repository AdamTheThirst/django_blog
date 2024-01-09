from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/list.html',
                  {'posts': posts})

def post_detail(request,id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No post found')

    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/detail.html',
                  {'post': post})

