from django.shortcuts import render, get_object_or_404
from .models import Thread, Post, Category
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def thread_detail(request, pk):


    thread = get_object_or_404(Thread, pk = pk)
    posts = Post.objects.filter(thread__pk = pk).order_by('created_at')[:30]
    # default amount of posts is 30, more can be requested from the API

    return render(request, 'forum/thread.html', {'thread': thread, 'posts': posts})

@login_required
def new_thread(request):
    return render(request, 'forum/post.html')

def category(request, catName):
    threads = Thread.objects.filter(category__name__iexact = catName).order_by('created_at')[:30]
    context = {'threads': threads, 'category': catName}
    return render(request, 'forum/subforum.html', context)
