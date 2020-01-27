"""django_sn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app import  views
from accounts import urls as ac_url
from groups import urls as group_urls
from posts import urls as post_urls

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name = 'index'),
    path('home/', views.HomePage.as_view(), name= 'index'),
    path('accounts/', include(ac_url, namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('group/', include(group_urls)),
    path('posts/', include(post_urls)),
    
]
