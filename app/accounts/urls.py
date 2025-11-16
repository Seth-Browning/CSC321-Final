from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.view_profile, name='profile-by-username'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
]