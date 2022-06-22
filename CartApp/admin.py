from django.contrib import admin
from models.models import *

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'price', 'quantity', 'information']
    list_per_page = 10
    search_fields = ['status']

admin.site.register(Cart, CartAdmin)
