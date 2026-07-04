from django.shortcuts import render
from .custom_signals import payment_successfull


# Create your views here.
class PaymentView:
    def make_payment(self, user, amount):
        # Logic to process payment
        # After successful payment, send the custom signal
        payment_successfull.send(sender=self.__class__, amount=amount, user=user)
