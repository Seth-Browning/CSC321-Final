from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.http import HttpResponse

# Create your views here.

def login(request):
    raise NotImplementedError()

def view_profile(request, username):
    print(username)
    profile = get_object_or_404(Profile, user__username = username)
    return render(request, 'accounts/profile.html', {'profile': profile})

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')