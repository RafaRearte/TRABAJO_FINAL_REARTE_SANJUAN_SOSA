from django.urls import path
from . import views


app_name='user'
urlpatterns = [
    path('login', views.login_request, name='user_login'),
    path('logout', views.logout_request, name='user_logout'),
    path('register', views.register, name='user_register'),
    path('register/update', views.user_update, name='user_update'),
    path('avatar/load', views.avatar_load, name='avatar_load'),
]