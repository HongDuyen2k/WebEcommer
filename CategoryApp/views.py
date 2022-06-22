from django.shortcuts import render
from models.models import *

# Create your views here.

def category_show_by_category(request, category, id):
    products = ''
    if(category == 'Clothes'):
        categories = Category.objects.filter(code=category, status='True')
        products = ClothesItem.objects.filter(category_id__in=categories)
    elif(category == 'Phone'):
        categories = Category.objects.filter(code=category, status='True')
        products = PhoneItem.objects.filter(category_id__in=categories)
    context = {
        'products': products,
        'categoryCode': category
    }
    return render(request, 'category.html',context)