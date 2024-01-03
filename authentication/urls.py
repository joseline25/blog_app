from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = "authentication"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='blog:home'), name='logout'), # it is not working
    # User profile
    path('profile/', views.profile, name='profile'),
]

""" 
- The LoginView is associated with the /login/ URL and uses the login.html
    template for rendering the login form.
- The LogoutView is associated with the /logout/ URL and redirects to the 
    home page (next_page='home') after the user logs out.
"""