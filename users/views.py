from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from schoollife.settings import EMAIL_HOST_USER
from .forms import UserRegister, UserUpdate, UserLogin
from .models import User, Follower


def register(request):
    if request.method == 'POST':    
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_mail(
                subject="welcome",
                message="welcome",
                recipient_list=[user.email],
                from_email=EMAIL_HOST_USER
            )
            return redirect('users:login')
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    form = UserLogin(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home:home')
        messages.error(request, 'Username or password invalid')
    context={
        'form':form
    }
    return render(request, 'login.html', context=context)




@login_required
def profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user_profile': user_profile})


def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def edit_profile(request):
    form = UserUpdate(request.POST or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile', user_id=request.user.id)
    return render(request, 'profile.html', {'form': form})


@login_required
def follow(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Follower.objects.get_or_create(follower_by_user=request.user, followee_user=other_user)
    return redirect('profile', user_id=user_id)


@login_required
def unfollow(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    Follower.objects.filter(follower_by_user=request.user, followee_user=other_user).delete()
    return redirect('profile', user_id=user_id)

