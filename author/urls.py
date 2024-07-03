from django.urls import path
from .views import UserRegistrationView,UserLoginForm,UserLogoutForm,ChangePasswordView,UserUpdate

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register' ),
    path('login/',UserLoginForm.as_view(),name='login' ),
    path('logout/',UserLogoutForm.as_view(),name='logout' ), 
    path('profile/',UserUpdate.as_view(),name='profile' ), 
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]