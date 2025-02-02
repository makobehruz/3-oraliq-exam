from django.contrib import admin
from .models import Post


class PostInline(admin.StackedInline):
    model = Post
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['name', 'desc']
    list_display = ('id', 'name', 'author', 'category', 'created_at')
    prepopulated_fields = {'desc': ('name',)}