from django.urls import path
from . import views

urlpatterns = [
    path('post-data/<int:pk>', views.view_post_data, name="post-data"),
    path('users/posts/<str:username>', views.posts_by_user),
    path('users/threads/<str:username>', views.threads_by_user),
    path('threads/<int:pk>', views.thread_data),
    path('posts/<int:pk>', views.post_data)
]