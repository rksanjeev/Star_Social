from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path(r"^$", views.PostList.as_view(), name="all"),
    path(r"new/$", views.CreatePost.as_view(), name="create"),
    path(r"by/(?P<username>[-\w]+)/$",views.UsersPost.as_view(),name="for_user"),
    path(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetails.as_view(),name="single"),
    path(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]