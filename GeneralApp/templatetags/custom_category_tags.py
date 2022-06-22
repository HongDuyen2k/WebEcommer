from django import template
from models.models import *
register = template.Library()

@register.simple_tag
def category_get_all():
    categories = Category.objects.filter(status='True')
    return categories;

@register.simple_tag
def category_get_limit():
    categories = Category.objects.filter(status='True').order_by('?')[:6]
    return categories;