from django.db import models
from catagory.models import Category
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):
    image=models.ImageField(upload_to='book/images/',blank=True,null=True)
    name = models.CharField(max_length=100)
    price=models.DecimalField(default=0,max_digits=12,decimal_places=2) 
    catagory= models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    discription=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

class borrow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(book,on_delete=models.CASCADE)
    boolinan=models.BooleanField(default=False)

class BookComment(models.Model):
    book=models.ForeignKey(book,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    comment=models.TextField()