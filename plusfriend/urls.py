from django.urls import path
from . import views

app_name = 'plusfriend'

urlpatterns = [
    path('friend', views.on_added),
    path('keyboard', views.on_init),
    path('friend/<user_key>', views.on_block),
    path('chat_room/<user_key>', views.on_leave),
    path('message', views.on_message),
    path('diary', views.post_list, name='post_list'),
]
