from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from author.models import UserAccount
from book.models import borrow


DEPOSIT = 1
WITHDRAWAL = 2
LOAN = 3
LOAN_PAID = 4
SENDMONEY=5

from transactions.forms import (
    DepositForm,
    
)
from transactions.models import Transaction





class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    pass
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # template e context data pass kora
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    pass
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount 
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
       
        
        return super().form_valid(form)

def reportView(request):
    transactions = Transaction.objects.filter(account=request.user.account)
    # print(transactions)
    return render(request, 'transactions/report.html', {'transactions': transactions})


def returnBook(request,id):
    transactions = Transaction.objects.get(id=id)
    borow=borrow.objects.get(user=request.user,book=transactions.book)
    account=UserAccount.objects.get(user=request.user)
    print(transactions.amount)
    account.balance+=transactions.amount


    tran=Transaction.objects.create(account=account,amount=transactions.amount,balance_after_transaction=account.balance,transaction_type=3)
    account.save()
    tran.save()
    borow.delete()
    transactions.delete()



    return redirect('report')