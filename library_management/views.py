from django.shortcuts import render,redirect
from book.models import book,borrow,BookComment
from catagory.models import Category
from author.models import UserAccount
from transactions.models import Transaction
from book.forms import CommentForm



def home(request, category_slug = None):
    data = book.objects.all()
    if category_slug is not None:
        categorys = Category.objects.get(slug = category_slug)
        data = book.objects.filter(catagory  = categorys)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories})



def carDetails(request,id):
    data=book.objects.get(id=id)  
    bookcomment=BookComment.objects.filter(book=data)
    borrows=borrow.objects.filter(user=request.user,book=data).exists()
    if request.method =='POST':
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.book=data
            comment.save()
            return redirect('bookdetails',id=id)
        else:
            pass
    else:
        commentForm=CommentForm()
        
    return render(request,'CarDtaile.html',{'data':data,'b':borrows,'form':commentForm,'allcomments':bookcomment})

    

def borrowBook(request,id):
    if request.method =='POST':
        bok=book.objects.get(id=id)
        user=UserAccount.objects.get(user=request.user)
        if user.balance>=bok.price:
            user.balance-=bok.price
            bok.quantity-=1
            bok.save()
            user.save()     
            tran=Transaction.objects.create(account=user,amount=bok.price,balance_after_transaction=user.balance,transaction_type=2,book=bok)
            tran.save()   
            order=borrow.objects.create(user=request.user,book=bok)
            order.save()
            return redirect('bookdetails',id=id)
        else:
            return redirect('bookdetails',id=id)
    else:
        return redirect('bookdetails',id=id)