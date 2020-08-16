from django.shortcuts import render, get_object_or_404
from .models import Post, PostImages


def post_list(request):
    posts = Post.objects.order_by('-updated_at')
    return render(request, 'blog.html', {'posts': posts})


def images_list(request):
    images = PostImages.objects.all()
    return render(request, 'post_detail.html', {'images': images})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})







