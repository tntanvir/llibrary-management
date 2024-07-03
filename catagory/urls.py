from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('add/', CategoryView.as_view(),name='category'),
    

]