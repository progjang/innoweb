from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import PlaceholderAuthForm

urlpatterns =[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    path('login/url/', views.RequestLoginViaUrlView.as_view(), name='request_login_via_url'),
    path('login/<uidb64>/<token>/', views.login_via_url, name='login_via_url'),
]