from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, value):
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(value)*100,
                    "product_data": {
                        "name": 'Item',
                        "description": 'what we will buy',
                    }
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=settings.PAYMENT_SUCCESS_URL,
        cancel_url=settings.PAYMENT_CANCEL_URL,
    )
    return redirect(checkout_session.url)

def payment_succeeded(request):
    return HttpResponse('Successful')

def payment_canceled(request):
    return HttpResponse('Cancel')