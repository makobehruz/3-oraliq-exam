from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'phone', 'created_at')
    search_fields = ['id', 'first_name', 'last_name']
