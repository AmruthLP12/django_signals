from django.shortcuts import render
from .custom_signals import payment_successfull

# Create your views here.


def payment_view(request):
    # Simulate a payment process
    amount = 100  # Example amount
    user = request.user  # Assuming the user is authenticated

    # Trigger the custom signal for successful payment
    payment_successfull.send(sender=None, amount=amount, user=user)

    return render(request, "payment_success.html", {"amount": amount})
