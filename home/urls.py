from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/add_comment/', views.add_comment, name='add_comment'),
    path('home/add_post/', views.add_post, name='add_post'),
    path('home/get_comments/', views.get_comments, name='get_comments'),
    path('home/get_num_comments/', views.get_num_comments, name='get_num_comments'),
    path('home/get_session_id/', views.get_session_id, name='get_session_id'),
    path('home/like_post/', views.like_post, name='like_post'),
    path('home/like_comment/', views.like_comment, name='like_comment'),
]