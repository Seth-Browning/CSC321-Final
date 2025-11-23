from django.urls import path
from . import views

urlpatterns = [
    path('post-data/<int:pk>', views.view_post_data, name="post-data")
]