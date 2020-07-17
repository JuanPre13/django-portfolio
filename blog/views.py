from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_posts(request):
    blogs = Blog.objects
    return render(request, 'blog/posts.html',
                            {'blogs':blogs} 
    )
def show_blog(request, id_blog):
    blog = get_object_or_404(Blog, pk=id_blog)
    return render(request, 'blog/post.html',
                            {'blog':blog}    
    )