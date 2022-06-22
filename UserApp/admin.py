from django.contrib import admin
from django.contrib.auth.models import User
from models.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login']
    list_filter = ['is_staff']

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','phone', 'gender', 'dateOfBirth', 'image_tag']

class UserAddressAdmin(admin.ModelAdmin):
    list_display=['user','noHome', 'street', 'city']


class CustomerMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'card']


admin.site.unregister(User)    
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(CustomerMember, CustomerMemberAdmin)