"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home,carDetails,borrowBook
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('author/',include('author.urls')),
    path('catagory/',include('catagory.urls')),
    path('transactions/',include('transactions.urls')),
    path('book/',include('book.urls')),
    path('details/<int:id>',carDetails,name='bookdetails'),
    path('borrow/<int:id>',borrowBook,name='borrow'),
    path('category/<slug:category_slug>/', home, name='category_wise_post')

    

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
