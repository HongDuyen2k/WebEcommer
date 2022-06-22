from django.contrib import admin
from models.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'details', 'status']


 
admin.site.register(Category, CategoryAdmin)