from django.contrib import admin
from models.models import *

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'comment','rate','created_at', 'status']

admin.site.register(Feedback, FeedbackAdmin)
