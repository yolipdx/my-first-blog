from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    """ post_list view 
        This is exactly what views are supposed to do: connect models and templates
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
