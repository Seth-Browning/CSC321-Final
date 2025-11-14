from django.urls import path
from . import views

urlpatterns = [
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail')
]