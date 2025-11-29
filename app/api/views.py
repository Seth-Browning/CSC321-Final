from django.http import JsonResponse, HttpRequest
from django.db.models import Q

from .serializers import PostSerializer, ThreadSerializer, ThreadSerializer_NoPosts
from forum.models import Post, Thread, Category

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

# +----------------------------------------------------------------------------
# |     User endpoints
# +----------------------------------------------------------------------------

@api_view(["GET"])
def posts_by_user(request: HttpRequest, username: str):
    """
    Gets all posts made by the specified user.

    Args:
        request (HttpRequest): The request object the API uses for responses.
        username (str): The name of the user whose posts are being filtered.

    Returns:
        Response: The list of the posts made by the user

    Note:
        This API function only accepts requests using the "GET" method.
    """

    posts = Post.objects.filter(author__username = username)
    serialized_posts = PostSerializer(posts, many=True)
    return Response(serialized_posts.data)

@api_view(["GET"]) 
def threads_by_user(request: HttpRequest, username: str) -> Response:
    """
    Gets all posts made by the specified user.

    Args:
        request (HttpRequest): Object containing all information about the request.
        username (str): The user whose threads are being filtered for.
    
    Returns:
        Response: The list of the threads made by the user

    Note:
        This API function only accepts requests using the "GET" method.

    """
    
    threads = Thread.objects.filter(creator__username = username)
    serialized_threads = ThreadSerializer(threads, many = True)
    return Response(serialized_threads.data)

# +----------------------------------------------------------------------------
# |     Thread endpoints
# +----------------------------------------------------------------------------

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def thread_list_api(request: HttpRequest):
    """
    Either lists all threads, or creates a new thread, depending on the request's method.

    Args:
        request (HttpRequest): Object containing all information about the request,
            including whether all threads should be listed or if a new thread should
            be created

    Notes:
        This API function only accepts requests using the "GET" or "POST" method. The
        requestor has to be authorized to make a new thread.
    """
    
    if request.method == "GET":
        threads = Thread.objects.all().order_by('-created_at')
        data= [
            {
                "id": t.id,
                "category": t.category.name,    
                # Since `category` is a foreign key, you need to reach through it to its name
                
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
def thread_detail_api(request: HttpRequest, pk: int):
    """
    Gets, Updates, or Deletes a thread depending on the request's method. Updates and deletes
    will only be applied if the requestor is authenticated and they're the creator of the thread.

    Args:
        request (HttpRequest): Object containing all of the inforamtion about the request.
            If the method type is "PUT", then the request's body should contain the data,
            to update the thread.
        pk (int): The key for the thread that is being acted on.
    
    Nots:
        This API function only supports the "GET", "PUT", and "DELETE" request methods.
    """

    try:
        thread = Thread.objects.get(pk = pk)
    except Thread.DoesNotExist:
        return Response({'error': "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def is_creator(request):
        return request.user.is_authenticated and request.user == thread.creator
    
    if request.method == "GET":
        serializer = ThreadSerializer(thread)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    
    # The Following actions require the requestor be the creator of the thread

    if not is_creator(request):
        return Response({'error': "Only the creator may modify threads"}, 
                        status= status.HTTP_403_FORBIDDEN)

    # Update the Thread's information
    if request.method == "PUT":
        data = request.data
        thread.title = data.get("title", thread.title)
        thread.category = \
            Category.objects.get(name__iexact=data.get("category", thread.category))
        thread.save()
        return Response({"status":"updated"}, status=status.HTTP_202_ACCEPTED)
    
    if request.method == "DELETE":
        thread.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_202_ACCEPTED)
    
    return Response({'errors': 'Invalid action'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# +----------------------------------------------------------------------------
# |     Post endpoints
# +----------------------------------------------------------------------------

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_api(request: HttpRequest):
    """
    Depending on the request method: either lists all posts, or the endpoint
    used for creating a new post. All posts must be attached to a thread,
    there is no such thing as an "orphan post."

    Args:
        request (HttpRequest): The object containing all the information
            for the request. The request's method determines the behavior.
            If a new post is being created, the thread id and post content
            must be given through a POST request.

    """

    if request.method == "GET":
        posts = Post.objects.all().order_by('-created_at')
        data = [
            {
                "id": t.id,
                "thread": t.thread.id,
                "author": t.author.username,
                "content": t.content,
                "created_at": t.created_at.isoformat()
            }
            for t in posts
        ]
        return Response(data)
    
    if not request.user.is_authenticated:
        return Response({'errors': "Authenticated Required"}, status=status.HTTP_403_FORBIDDEN)
    
    data = request.data

    try:
        thread = Thread.objects.get(pk= data.get("thread"))
    except Thread.DoesNotExist:
        return Response({'errors': "Thread does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    post = Post.objects.create(
        thread= thread,
        author= request.user,
        content = data.get("content")
    )

    return Response({
        "status": "Post created",
        "id": post.id
    }, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail_api(request: HttpRequest, pk: int):
    """
    Depending on the method: Retrieves a posts's information, update's a 
    posts's content, or deletes a post.

    Args:
        request (HttpRequest):
            The request, containing the method and, if the method is `PUT`,
            the new content for the post.

        pk (int):
            The id of the post being accessed.
    
    Returns:
        If the request method was POST, then the inforamation from the specified
        post. Otherwise, a simple status object is returned.
    """

    try:
        post = Post.objects.get(pk = pk)
    except Post.DoesNotExist:
        return Response({'errors': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def is_creator(request: HttpRequest):
        return request.user.is_authenticated and request.user == post.author
    
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if not is_creator(request):
        return Response({"errors": "Only owner may modify post"}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == "PUT":
        data = request.data
        post.content = data.get("content", post.content)
        post.save()
        return Response({"status": "updated"}, status=status.HTTP_202_ACCEPTED)
    
    if request.method == "DELETE":
        post.delete()
        return Response({"status": "removed"}, status=status.HTTP_202_ACCEPTED)
    
    return Response({"errors": "Invalid action"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# +----------------------------------------------------------------------------
# |     Seach endpoints
# +----------------------------------------------------------------------------

@api_view(["GET"])
def search(request: HttpRequest):
    """
    Searches threads and posts for content that contains the text given
    by the `?q=` URL parameter.

    Args:
        request (HttpRequest): The URL object containing the `?q=`
            parameter, which defines what content to seatch for.
    """

    q = request.GET.get("q", "")

    threads = Thread.objects.filter(
        Q(title__icontains= q) |
        Q(category__name__icontains= q) |
        Q(posts__content__icontains= q)
    ).distinct()

    threads_serial = [
        {
            "id": t.id,
            "category": t.category.name,
            "creator": t.creator.username,
            "title": t.title,
            "created_at": t.created_at.isoformat()
        }
        for t in threads
    ]

    posts = Post.objects.filter(
        Q(content__icontains= q) |
        Q(author__username__icontains= q)
    )

    posts_serial = [
        {
            "id": t.id,
            "thread": ThreadSerializer_NoPosts(t.thread).data,
            "author": t.author.username,
            "content": t.content,
            "created_at": t.created_at.isoformat()
        }
        for t in posts
    ]

    return JsonResponse({"posts": posts_serial, "threads": threads_serial}, status=status.HTTP_200_OK)

# +----------------------------------------------------------------------------
# |     Report endpoints
# +----------------------------------------------------------------------------

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