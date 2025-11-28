from django.shortcuts import render

from forum.models import Thread

# Create your views here.
def home(request):
    recent_threads = Thread.objects.all().order_by("created_at")[:30]
    return render(request, 'core/home.html', {"threads": recent_threads})