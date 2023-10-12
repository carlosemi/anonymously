from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/add_comment/', views.add_comment, name='add_comment')
]