from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .serializers import PostSerializer, ThreadSerializer
from forum.models import Post, Thread

def view_post_data(request, pk):
    post = get_object_or_404(Post, pk = pk)
    serialized = PostSerializer(post)
    return JsonResponse(serialized.data)

def posts_by_user(request, username):
    # posts = get_list_or_404(Post, author__username = username)
    posts = Post.objects.filter(author__username = username)
    serialized_posts = PostSerializer(posts, many=True)
    return JsonResponse(serialized_posts.data, safe=False)
    

def threads_by_user(request, username):
    # threads = get_list_or_404(Thread, creator__username = username)
    threads = Thread.objects.filter(creator__username = username)
    serialized_threads = ThreadSerializer(threads, many = True)
    return JsonResponse(serialized_threads.data, safe=False)

def thread_data(request, threadId):
    raise NotImplementedError()

def post_data(request, postId):
    raise NotImplementedError()

def delete_thread(request, threadId):
    raise NotImplementedError()

def deleted_post(request, postId):
    raise NotImplementedError()

def edit_thread(request, threadId):
    raise NotImplementedError()

def edit_post(request, postId):
    raise NotImplementedError()

def report_user(request, userId):
    raise NotImplementedError()

def report_post(request, postId):
    raise NotImplementedError()

def report_thread(request, threadId):
    raise NotImplementedError()