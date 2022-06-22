from django import template
from models.models import *
register = template.Library()

@register.simple_tag
def cart_tag_total_amount(userId):
    all_cart_product = Cart.objects.filter(user_id=userId, status='Draft')
    total_amount = 0
    for p in all_cart_product:
        total_amount += p.price * p.quantity
    return "{:,.1f}".format(total_amount)

@register.simple_tag
def cart_tag_total_quantity(userId):
    all_cart_product = Cart.objects.filter(user_id=userId, status='Draft')
    total_quantity = 0
    for p in all_cart_product:
        total_quantity += p.quantity
    return total_quantity

@register.simple_tag
def cart_tag_get_all_product(userId):
    cart_item = Cart.objects.filter(user_id=userId, status='Draft')[:2]
    return cart_item