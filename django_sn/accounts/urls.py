from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('signup', views.SignUp.as_view()),
    path('login', auth_views.LoginView.as_view(template_name = 'accounts/login.html')),
    path('logout', auth_views.LogoutView.as_view()),
    
]
