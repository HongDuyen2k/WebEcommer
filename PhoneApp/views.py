from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from models.models import *


# Create your views here.
@login_required(login_url='/user/user-login')
def phone_add_now_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkCart = Cart.objects.filter(phoneItem_id=id, user_id=current_user.id, status='Draft')
    phoneItem = PhoneItem.objects.get(id=id)

    if request.method == "POST":
        information = 'Màu sắc: ' + request.POST['color_phone']
        if checkCart:
            data = Cart.objects.get(phoneItem_id=id, user_id=current_user.id, status='Draft')
            data.quantity = int(request.POST['quantity_phone'])
            data.information = information
            data.save()
        else:
            data = Cart()
            data.name = phoneItem.name
            data.price = phoneItem.price * ((100 - phoneItem.discount) % 100);
            data.quantity = int(request.POST['quantity_phone'])
            data.status = 'Draft'
            data.user_id = current_user.id
            data.phoneItem_id = id
            data.information = information
            data.save()
        messages.success(request, 'Bạn đã thêm sản phẩm vào giỏ thành công')
        return HttpResponseRedirect(url)
    else:
        if checkCart:
            data = Cart.objects.get(phoneItem_id=id, user_id=current_user.id, status='Draft')
            data.quantity += 1
            data.save()
        else:
            data = Cart()
            data.name = phoneItem.name
            data.price = phoneItem.price * ((100 - phoneItem.discount) % 100);
            data.quantity = 1
            data.status = 'Draft'
            data.user_id = current_user.id
            data.phoneItem_id = id
            data.save()
        messages.success(request, 'Bạn đã thêm sản phẩm vào giỏ thành công')
        return HttpResponseRedirect(url)

def phone_details(request, id):
    phoneItem = PhoneItem.objects.get(id=id)
    phone = Phone.objects.get(id=phoneItem.phone_id)
    imagePhone = ImagePhone.objects.filter(phone_id=phone.id)
    colorPhone = ColorPhone.objects.filter(phone_id=phone.id)
    randomProduct = PhoneItem.objects.all().order_by('?')[:15]
    feedbacks = Feedback.objects.filter(phoneItem_id=phoneItem.id, status='True')
    total_rate = 0;

    for feedback in feedbacks:
        total_rate += feedback.rate
    if(len(feedbacks) > 0):        
        total_rate = round(total_rate/len(feedbacks), 2)

    context = {
        'phoneItem': phoneItem,
        'phone': phone,
        'imagePhone': imagePhone,
        'colorPhone': colorPhone,
        'randomProduct': randomProduct,
        'feedbacks': feedbacks,
        'total_rate': total_rate
    }
    return render(request, 'phone-details.html', context)