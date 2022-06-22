from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from models.models import *

# Create your views here.

@login_required(login_url='/user/user-login')
def cart_details(request):
    current_user = request.user
    all_cart_product = Cart.objects.filter(user_id=current_user.id, status='Draft')
    total_amount = 0
    total_quantity = 0

    for p in all_cart_product:
        total_amount += p.price * p.quantity
        total_quantity += p.quantity

    context = {
        'all_cart_product': all_cart_product,
        'total_amount': total_amount,
        'total_quantity': total_quantity
    }
    return render(request, 'cart-details.html', context)

def cart_delete(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart_product = Cart.objects.filter(id=id, user_id=current_user.id)
    cart_product.delete()
    messages.warning(request, 'Sản phẩm của bạn đã bị xóa.')
    return HttpResponseRedirect(url)

