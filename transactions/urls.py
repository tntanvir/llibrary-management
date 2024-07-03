from django.urls import path
from .views import DepositMoneyView,reportView,returnBook

urlpatterns = [
 
    path('deposit/',DepositMoneyView.as_view(),name='deposit'),
    path('report/',reportView,name='report'),
    path('return/<int:id>',returnBook,name='return'),
    
    

]
