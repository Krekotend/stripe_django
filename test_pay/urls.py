from django.urls import path
from . import views

urlpatterns = [
    path('order_page/<int:value>', views.create_checkout_session),
    path("success/", views.payment_succeeded),
    path("cancel/", views.payment_canceled)
]