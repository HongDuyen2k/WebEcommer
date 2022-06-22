from django.contrib import admin
from models.models import *

# Register your models here.

class ImageClothesInline(admin.TabularInline):
    model = ImageClothes
    readonly_fields = ['image_tag']
    extra = 1

class ColorClothesInline(admin.TabularInline):
    model = ColorClothes
    extra = 1

class SizeClothesInline(admin.TabularInline):
    model = SizeClothes
    extra = 1

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'type', 'madeIn', 'manufactureDate']
    list_per_page = 10
    search_fields = ['name', 'size']
    inlines = [ImageClothesInline, ColorClothesInline, SizeClothesInline]

class ClothesItemAdmin(admin.ModelAdmin):
    list_display = ['clothes', 'name', 'barcode', 'price', 'quantity', 'category', 'image_tag']
    list_per_page = 10
    search_fields = ['name', 'price']

admin.site.register(Clothes, ClothesAdmin)
admin.site.register(ClothesItem, ClothesItemAdmin)
