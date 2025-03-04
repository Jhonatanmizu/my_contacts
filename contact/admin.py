"""Admin models"""
from django.contrib import admin

from contact.models import Category, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """" Contact admin """
    list_display = ("id", 'name', 'email', 'phone_number',
                    'created_at', 'is_visible')
    ordering = ('created_at',)
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone_number', 'created_at')
    list_per_page = 20
    list_max_show_all = 100
    list_editable = ('is_visible',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """" Category admin """
    list_display = ("id", 'name', 'created_at',)
    ordering = ('created_at',)
    list_filter = ('created_at',)
    search_fields = ('name',)
    list_per_page = 20
    list_max_show_all = 100
