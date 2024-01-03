from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # list of posts
    path('', views.home, name='home'),
    # details of a post
    path('post_detail/<int:pk>/',
         views.post_detail, name='post_detail'),
    # create a post
    path('post_create/', views.post_create, name='post_create'),
    # edit a post
    path('post_edit/<int:pk>/',
         views.post_edit, name='post_edit'),
    # detail of a post
    path('post_detail/<int:pk>/',
         views.post_edit, name='post_detail'),
    # create a post
    path('post_create/', views.post_create, name='post_create'),
    # delete a post
    path('post_delete/<int:pk>/',
         views.post_delete, name='post_delete'),
    
    
    # details of a category
    path('category_detail/<int:pk>/',
         views.category_detail, name='category_detail'),
    # filter by tag
    path('tag_detail/<int:pk>/',
         views.tag_detail, name='tag_detail'),
    path('search_post/', views.search_post, name='search_post'),
    
#     
]
