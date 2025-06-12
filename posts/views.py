from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def post_detail(request, post_id):
    return render(request, 'post_detail.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def explore(request):
    return render(request, 'explore.html')

def reels(request):
    return render(request, 'reels.html')

def notifications(request):
    return render(request, 'notifications.html')