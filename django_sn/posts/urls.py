from django.urls import path   
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view() , name = 'all'),
    path('new/', views.CreatePost.as_view(), name = 'create'),
    path('user/<username>', views.UsersPost.as_view(), name= 'for_user'),
    path('user/<username>/<id>',views.PostDetails.as_view(), name = 'details'),
    path('delete/<id>', views.DeletePost.as_view(), name = 'delete'),

]