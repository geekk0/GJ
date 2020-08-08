from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-updated_at')
    return render(request, 'blog.html', {'posts': posts})

def images_list(request):
    images = Post_images.objects.filter(photo_of__contains=Post.title)
    return render(request, 'post_detail.html', {'images': images})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})





