from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CategoryForms
from .models import Category
# Create your views here.


class CategoryView(CreateView):
    model=Category
    form_class=CategoryForms
    template_name='catagory.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        return super().form_valid(form)