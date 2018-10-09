from django.contrib import admin
from .models import KakaoPost
# Register your models here.

@admin.register(KakaoPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'photo', 'created_at']