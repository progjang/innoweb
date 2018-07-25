from django.contrib import admin
from .models import Post, Maker, Device, Resource
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'updated_at',]
    list_display_links = ['name']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['get_photo', 'name', 'get_makername', 'created_at',]
    list_display_links = ['name']

    def get_makername(self,obj):
        return obj.maker.name
    
    def get_photo(self,obj):
        img_url = "<img src=" + obj.photo.url + " height='100' />"
        return mark_safe(img_url)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'contenturl', 'created_at',]
    list_display_links = ['title']
    search_fields = ['title']

