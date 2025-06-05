from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Home View
class HomeView(TemplateView):
    template_name = 'home.html'

# Profile View
class ProfileView(TemplateView):
    template_name = 'profile.html'

# Explore View
class ExploreView(TemplateView):
    template_name = 'explore.html'

# Search View
class SearchView(TemplateView):
    template_name = 'search.html'

# Reels View
class ReelsView(TemplateView):
    template_name = 'reels.html'

# Messages View
class MessagesView( TemplateView):
    template_name = 'messages.html'

# Notifications View
class NotificationsView(TemplateView):
    template_name = 'notifications.html'


# Create Post View
class CreateView(TemplateView):
    template_name = 'create.html'


# Threads View
class ThreadsView(TemplateView):
    template_name = 'threads.html'


# Settings View
class SettingsView(TemplateView):
    template_name = 'settings.html'


# Authentication Views
class LoginView(TemplateView):
    template_name = 'auth/login.html'

class SignupView(TemplateView):
    template_name = 'auth/signup.html'

