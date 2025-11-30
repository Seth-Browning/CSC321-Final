from django.urls import path
from . import views

urlpatterns = [
    path('users/posts/<str:username>', views.posts_by_user),
    path('users/threads/<str:username>', views.threads_by_user),
    path('users/<str:username>', views.user_detail_api),

    path('threads/', views.thread_list_api),
    path('threads/<int:pk>', views.thread_detail_api),
    path('posts/', views.post_list_api),
    path('posts/<int:pk>', views.post_detail_api),

    path('report/threads/<int:pk>', views.report_thread),
    path('report/posts/<int:pk>', views.report_post),
    path('report/users/<str:username>', views.report_user),

    path('search/', views.search)
]