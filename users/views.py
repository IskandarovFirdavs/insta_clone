from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegister, UserUpdate
from .models import User, Follower


def register(request):
    if request.method == 'POST':    
        print("Registering user")
        print(request.POST)
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("User registered successfully")
            login(request, user)
            return redirect('profile', user_id=user.id)
    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})


def profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user_profile': user_profile})


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