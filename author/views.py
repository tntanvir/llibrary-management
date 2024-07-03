from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserRegistrationForm,UpdateUserForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import UserAccount

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'


class UserRegistrationView(FormView):
    template_name = 'user_register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        # print(form.cleaned_data)
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    

class UserLoginForm(LoginView):
    template_name='user_login.html'
    def get_success_url(self) :
        return reverse_lazy('home')
    
class UserLogoutForm(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class UserUpdate(UpdateView):
    model=User
    form_class=UpdateUserForm
    template_name='profile.html'
    success_url = reverse_lazy('profile')
    def get_object(self):
        return self.request.user

