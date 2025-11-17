from django.urls import path
from . import views

urlpatterns = [
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('new-thread/', views.new_thread, name="new_thread"),
    path('category/<str:catName>', views.category, name="forum_category")
]