from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from models.models import *

# Create your views here.
@login_required(login_url='/user/user-login')
def feedback_add(request, category, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    if request.method == 'POST':
        data = Feedback()
        data.rate = int(request.POST['rate'])
        data.subject = request.POST['subject']
        data.comment = request.POST['comment']
        data.status = 'True'
        data.user_id = current_user.id
        
        if(category == 'Clothes'):
            data.clothesItem_id = id
        elif(category== 'Phone'):
            data.phoneItem_id = id
        data.save()
    messages.success(request, 'Bạn đã thêm thành công đánh giá sản phẩm')
    return HttpResponseRedirect(url)