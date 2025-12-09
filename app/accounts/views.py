from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from forum.models import Thread, Post
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

@login_required
def view_profile(request, username):
    print(username)
    profile = get_object_or_404(Profile, user__username = username)
    threads = Thread.objects.filter(creator__username = username)
    return render(request, 'accounts/profile.html', {'profile': profile, 'threads': threads})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def settings(request: HttpRequest):
    profile = get_object_or_404(Profile, user__username = request.user.username)
    return render(request, 'accounts/settings.html', {'profile': profile})

@login_required
def change_password(request: HttpRequest):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # keep user logged in
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'form': form})