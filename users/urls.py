from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('explore/', views.ExploreView.as_view(), name='explore'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('reels/', views.ReelsView.as_view(), name='reels'),
    path('messages/', views.MessagesView.as_view(), name='messages'),
    path('notifications/', views.NotificationsView.as_view(), name='notifications'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('threads/', views.ThreadsView.as_view(), name='threads'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]
