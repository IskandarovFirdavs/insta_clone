from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('explore/', views.explore, name='explore'),
    path('reels/', views.reels, name='reels'),
    path('notifications/', views.notifications, name='notifications'),
]