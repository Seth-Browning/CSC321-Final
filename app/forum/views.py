from django.shortcuts import render, get_object_or_404
from .models import Thread, Post

# Create your views here.

def thread_list(request):
    threads = Thread.objects.all().order_by('-created_at')
    return render(request, 'forum/thread_list.html', {"threads": threads})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk = pk)
    posts = thread.posts.all()
    return render(request, 'forum/thread_detail.html', {"thread": thread, "posts": posts})