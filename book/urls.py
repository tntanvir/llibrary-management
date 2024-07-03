from django.urls import path
from .views import bookPost

urlpatterns = [
    path('add/', bookPost,name='bookadd'),
]