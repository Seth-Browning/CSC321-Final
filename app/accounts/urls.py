from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/<str:username>/', views.view_profile, name='profile-by-username'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", next_page="/"), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('settings/', views.settings, name="settings"),
    path('change-password/', views.change_password, name="change_password"),
    path('change-username/', views.change_username, name="change_username")
]