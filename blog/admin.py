from django.contrib import admin
from .models import Post, Device, Resource
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'created_at',]
    list_display_links = ['name']

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'contenturl', 'created_at',]
    list_display_links = ['title']
    search_fields = ['title']

