from django.contrib import admin
from models.models import *

# Register your models here.

class VoucherAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'discountPercent']

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'totalPriceBefore', 'totalPriceAfter', 'information', 'note', 'created_at', 'status']


admin.site.register(Voucher, VoucherAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(Order, OrderAdmin)
