from django.shortcuts import redirect, render
from models.models import *

# Create your views here.

def general_home(request):
    clothesItem = ClothesItem.objects.all().order_by('id')[:8]
    phoneItem = PhoneItem.objects.all().order_by('id')[:8]

    context = {
        'clothesItem': clothesItem,
        'phoneItem': phoneItem
    }
    return render(request, 'home.html', context)

def general_search_product(request):
    if request.method == 'POST':
        search = request.POST['search_product']
        category_product = request.POST['category_product']
        category = Category.objects.get(id=category_product)
        if(category.code == 'Clothes'):
            products = ClothesItem.objects.filter(name__contains=search)
        elif(category.code == 'Phone'):
            products = PhoneItem.objects.filter(name__contains=search)
    else:
        return redirect('cart_details')
    context = {
        'search': search,
        'products': products,
        'categoryCode': category.code
    }
    return render(request, 'search.html', context)