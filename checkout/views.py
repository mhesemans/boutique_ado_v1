from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at this time!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SJQqQK4fk4HNOrJI1O30JEd1xvh8pAOP4Hl5xRQqg3pRHYNJWCkB4yO4K1ABkytkZZzYf3blQx9P6G7DprmFoZM00Ovx0SmOG',
        'client_secret': 'sk_test_51SJQqQK4fk4HNOrJhOEXCJKCxZ9429Cc8MK4SYzfr34oPYPWcl8rNxEPVqheMAiboBcoUh7csNy8dTXLbpItV7MC00tvrNrppG',
    }

    return render(request, template, context)
