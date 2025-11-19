from django.urls import reverse

def global_urls(request):
    profile_url = None
    if request.user.is_authenticated:
        profile_url = reverse('profile-by-username', kwargs={'username': request.user.username})
    
    return {
        'GLOBAL_PROFILE_URL': profile_url,
        'GLOBAL_REGISTER_URL': reverse('register'),
        "GLOBAL_LOGIN_URL": reverse('login')
    }