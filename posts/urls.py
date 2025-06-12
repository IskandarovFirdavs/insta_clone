from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('explore/', views.explore, name='explore'),
    path('reels/', views.reels, name='reels'),
    path('notifications/', views.notifications, name='notifications'),
]