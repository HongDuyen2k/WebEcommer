from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from models.models import *


# Create your views here.
@login_required(login_url='/user/user-login')
def clothes_add_now_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkCart = Cart.objects.filter(clothesItem_id=id, user_id=current_user.id, status='Draft')
    clothesItem = ClothesItem.objects.get(id=id)

    if request.method == "POST":
        information = 'Size: ' + request.POST['size_clothes'] + '- Màu sắc: ' + request.POST['color_clothes']
        if checkCart:
            data = Cart.objects.get(clothesItem_id=id, user_id=current_user.id, status='Draft')
            data.quantity = int(request.POST['quantity_clothes'])
            data.information = information
            data.save()
        else:
            data = Cart()
            data.name = clothesItem.name
            data.price = clothesItem.price * ((100 - clothesItem.discount) % 100);
            data.quantity = int(request.POST['quantity_clothes'])
            data.status = 'Draft'
            data.user_id = current_user.id
            data.clothesItem_id = id
            data.information = information
            data.save()
        messages.success(request, 'Bạn đã thêm sản phẩm vào giỏ thành công')
        return HttpResponseRedirect(url)
    else:
        if checkCart:
            data = Cart.objects.get(clothesItem_id=id, user_id=current_user.id, status='Draft')
            data.quantity += 1
            data.save()
        else:
            data = Cart()
            data.name = clothesItem.name
            data.price = clothesItem.price * ((100 - clothesItem.discount) % 100);
            data.quantity = 1
            data.status = 'Draft'
            data.user_id = current_user.id
            data.clothesItem_id = id
            data.save()
        messages.success(request, 'Bạn đã thêm sản phẩm vào giỏ thành công')
        return HttpResponseRedirect(url)

def clothes_details(request, id):
    clothesItem = ClothesItem.objects.get(id=id)
    clothes = Clothes.objects.get(id=clothesItem.clothes_id)
    imageClothes = ImageClothes.objects.filter(clothes_id=clothes.id)
    colorClothes = ColorClothes.objects.filter(clothes_id=clothes.id)
    sizeClothes = SizeClothes.objects.filter(clothes_id=clothes.id)
    randomProduct = ClothesItem.objects.all().order_by('?')[:15]
    feedbacks = Feedback.objects.filter(clothesItem_id=clothesItem.id, status='True')
    total_rate = 0;
    
    for feedback in feedbacks:
        total_rate += feedback.rate
    if(len(feedbacks) > 0):        
        total_rate = round(total_rate/len(feedbacks), 2)

    context = {
        'clothesItem': clothesItem,
        'clothes': clothes,
        'imageClothes': imageClothes,
        'colorClothes': colorClothes,
        'sizeClothes': sizeClothes,
        'randomProduct': randomProduct,
        'feedbacks': feedbacks,
        'total_rate': total_rate
    }
    return render(request, 'clothes-details.html', context)