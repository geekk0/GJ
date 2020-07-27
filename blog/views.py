from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-updated_at')
    return render(request, './blog.html', {'posts': posts})

