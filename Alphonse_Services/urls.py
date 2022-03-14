from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/login', views.login_view, name='login'),
    path('users/profile', views.profile, name='profile')
]
