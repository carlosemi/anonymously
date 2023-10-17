from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/add_comment/', views.add_comment, name='add_comment'),
    path('home/add_post/', views.add_post, name='add_post'),
    path('home/get_comments/', views.get_comments, name='get_comments'),
]