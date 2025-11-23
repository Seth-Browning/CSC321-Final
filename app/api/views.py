from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .serializers import PostSerializer
from forum.models import Post, Thread

def view_post_data(request, pk):
    post = get_object_or_404(Post, pk = pk)
    serialized = PostSerializer(post)
    return JsonResponse(serialized.data)