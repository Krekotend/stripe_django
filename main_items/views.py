from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Item


def get_item(request, value: int):
    item = get_object_or_404(Item, id=value)
    return render(request, 'main_items/item.html', {
        'item': item
    })


def get_buy(request, value: int):
    item = get_object_or_404(Item, id=value)
    price = item.price
    return HttpResponseRedirect(f'/order_page/{price}')
