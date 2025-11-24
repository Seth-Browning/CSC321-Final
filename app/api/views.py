from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpRequest
from .serializers import PostSerializer, ThreadSerializer
from forum.models import Post, Thread, Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def posts_by_user(request, username):
    # posts = get_list_or_404(Post, author__username = username)
    posts = Post.objects.filter(author__username = username)
    serialized_posts = PostSerializer(posts, many=True)
    return Response(serialized_posts.data)

@api_view(["GET"]) 
def threads_by_user(request, username):
    # threads = get_list_or_404(Thread, creator__username = username)
    threads = Thread.objects.filter(creator__username = username)
    serialized_threads = ThreadSerializer(threads, many = True)
    return Response(serialized_threads.data)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def thread_list_api(request: HttpRequest):
    """
    API endpoint for threads in general. GET requests list all threads,
    POST request create a new thread
    """
    
    if request.method == "GET":
        threads = Thread.objects.all().order_by('-created_at')
        data= [
            {
                "id": t.id,
                "category": t.category.name,
                "title": t.title,
                "creator": t.creator.username,
                "created_at": t.created_at.isoformat()
            }
            for t in threads
        ]
        return JsonResponse(data, safe=False)
    
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication Required'}, status=status.HTTP_403_FORBIDDEN)
    
    data = request.data

    cat = Category.objects.get(name=data.get("category"))

    thread = Thread.objects.create(
        category= cat,
        title= data.get("title"),
        creator= request.user
    )

    return Response({
        'status': 'Created',
        'id': thread.id,
    }, status= status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def thread_detail_api(request: HttpRequest, pk):
    """
    API endpoint for a specific thread.
    """

    try:
        thread = Thread.objects.get(pk = pk)
    except Thread.DoesNotExist:
        return Response({'error': "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    

    def is_creator(request):
        return request.user.is_authenticated and request.user == thread.creator
    
    if request.method == "GET":
        serializer = ThreadSerializer(thread)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # The Following actions require the requestor be the creator of the thread

    if not is_creator(request):
        return Response({'error': "Only the creator may modify threads"}, 
                        status= status.HTTP_403_FORBIDDEN)

    if request.method == "PUT":
        data = request.data
        thread.title = data.get("title", thread.title)
        thread.category = data.get("category", thread.category)
        thread.save()
        return Response({"status":"updated"}, status=status.HTTP_202_ACCEPTED)
    
    if request.method == "DELETE":
        thread.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_202_ACCEPTED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def report_user(request, userId):
    raise NotImplementedError()

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def report_post(request, postId):
    raise NotImplementedError()

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def report_thread(request, threadId):
    raise NotImplementedError()