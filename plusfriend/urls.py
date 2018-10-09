from django.urls import path
from . import views

app_name = 'plusfriend'

urlpatterns = [
    url(r'^keyboard$', views.on_init),
    url(r'^friend$', views.on_added),
    url(r'^friend/<user_key>$', views.on_block),
    url(r'^chat_room/<user_key>$', views.on_leave),
    url(r'^message$', views.on_message),
    url(r'^diary/$', views.post_list, name='post_list'),
]
