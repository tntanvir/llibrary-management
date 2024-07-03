from django.db import models
from author.models import UserAccount
from .constains import TRANSACTIONS_TYPE
from book.models import book
# Create your models here.
class Transaction(models.Model):
    account=models.ForeignKey(UserAccount, related_name='transaction',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction=models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type=models.IntegerField(choices=TRANSACTIONS_TYPE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    book=models.ForeignKey(book, null=True, blank=True,on_delete=models.CASCADE)
    class Meta:
        ordering=['timestamp']