from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from UserApp.forms import RegisterForm
from models.models import *

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('general_home')
        else:
            messages.warning(request, 'Tài khoản hoặc mật khẩu không đúng.')
    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('general_home')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password  = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('general_home');
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def user_profile(request):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkProfile = UserProfile.objects.filter(user_id=current_user.id) 
    checkAddress = UserAddress.objects.filter(user_id=current_user.id)

    if request.method == 'POST':
        if checkProfile:
            data = UserProfile.objects.get(user_id=current_user.id) 
        else:
            data = UserProfile()
        data.gender = request.POST['gender']
        data.dateOfBirth = request.POST['dateOfBirth']
        data.phone = request.POST['phone']
        data.user_id = current_user.id
        data.save()

        if checkAddress:
            userAddress = UserAddress.objects.get(user_id=current_user.id)
        else:
            userAddress = UserAddress()
        userAddress.noHome = request.POST['noHome']
        userAddress.street = request.POST['street']
        userAddress.district = request.POST['district']
        userAddress.city = request.POST['city']
        userAddress.user_id = current_user.id
        userAddress.save()
        messages.success(request, 'Bạn đã cập nhập thông tin cá nhân thành công')
        return HttpResponseRedirect(url)
    context = {
        'user': current_user
    }   
    
    return render(request, 'user/user-profile.html', context)