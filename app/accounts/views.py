from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

def login_user(request):
    raise NotImplementedError()

@login_required
def view_profile(request, username):
    print(username)
    profile = get_object_or_404(Profile, user__username = username)
    return render(request, 'accounts/profile.html', {'profile': profile})

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm

    return render(request, 'accounts/register.html', {'form': form})
