from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    """Defines the post list"""
    # Let's see what happens if I call ALL posts
    # posts = Post.objects.filter(published_date__lte = timezone.now())
    posts = Post.objects.all()
    posts.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
