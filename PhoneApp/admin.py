from django.contrib import admin
from models.models import *

# Register your models here.

class ImagePhoneInline(admin.TabularInline):
    model = ImagePhone
    readonly_fields = ['image_tag']
    extra = 1

class ColorPhoneInline(admin.TabularInline):
    model = ColorPhone
    extra = 1
    
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'version', 'madeIn', 'yearOfManufacture', 'type', 'ram', 'memory']
    list_per_page = 10
    search_fields = ['name', 'yearOfManufacture']
    inlines = [ImagePhoneInline, ColorPhoneInline]

class PhoneItemAdmin(admin.ModelAdmin):
    list_display = ['phone', 'name', 'barcode', 'price', 'quantity', 'category', 'image_tag']
    list_per_page = 10
    search_fields = ['name', 'price']

admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneItem, PhoneItemAdmin)

