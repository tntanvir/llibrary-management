from django.shortcuts import render
from .forms import BookForm
from .models import book
from django.shortcuts import redirect

# Create your views here.
def bookPost(request):
    if request.method =='POST':
        forms=BookForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.instance.author=request.user
            forms.save()
            return redirect('home')
    else:
        forms=BookForm()
    return render(request, 'book.html', {'form':forms})

