from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:value>', views.get_item),
    path('buy/<int:value>', views.get_buy),
]