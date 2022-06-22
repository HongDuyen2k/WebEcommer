from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from models.models import *
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

@login_required(login_url='/user/user-login')
def order_cart_product(request):
    current_user = request.user
    all_cart_details = Cart.objects.filter(user_id=current_user.id, status='Draft')
    shipments = Shipment.objects.all()
    total_amount = 0
    for i in all_cart_details:
        total_amount += i.price
        if i.information == '':
            messages.warning(request, 'Vui lòng xác nhận thông tin của tất cả sản phẩm.')
            return redirect('cart_details')

    context = {
        'current_user': current_user,
        'all_cart_details': all_cart_details,
        'total_amount': total_amount,
        'shipments': shipments
    }
    return render(request, 'checkout.html', context)

@login_required(login_url='/user/user-login')
def order_confirm_before(request):
    current_user = request.user
    all_cart_details = Cart.objects.filter(user_id=current_user.id, status='Draft')

    total_amount_before = 0
    information = ''
    for i in all_cart_details:
        total_amount_before += i.price 
        information += str(i.id) + ' - '
    total_amount_after = total_amount_before

    voucherId = ''
    voucherPrice= ''
    if request.POST['voucher']:
        checkVoucher = Voucher.objects.filter(code=request.POST['voucher'])
        if checkVoucher:
            voucher = Voucher.objects.get(code=request.POST['voucher'])
            voucherId = voucher.id
            voucherPrice = voucher.discountPercent
            total_amount_after = total_amount_before * (1 - voucherPrice/100)

    note = ''
    if request.POST['note']:
        note = request.POST['note']

    shipment = Shipment.objects.get(id=request.POST['shipment'])
    total_amount_after = total_amount_after - shipment.price 

    checkOrder = Order.objects.filter(user_id=current_user.id, status='Draft')
    if checkOrder:
        order = Order.objects.get(user_id=current_user.id, status='Draft')
    else:
        order = Order()
    order.totalPriceBefore = total_amount_before
    order.totalPriceAfter = total_amount_after
    order.information = information
    order.note = note
    order.status = 'Draft'
    order.user_id = current_user.id
    order.voucher_id = voucherId
    order.shipment_id = request.POST['shipment']
    order.save()
    
    context = {
        'current_user': current_user,
        'all_cart_details': all_cart_details,
        'total_amount_before': total_amount_before,
        'total_amount_after': total_amount_after,
        'voucher_price': voucherPrice,
        'shipment': shipment,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'payment-confirmation.html', context)

@login_required(login_url='/user/user-login')
def order_details(request):
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)

    context = {
      'orders': orders
    }
    return render(request, 'order-detail.html', context)