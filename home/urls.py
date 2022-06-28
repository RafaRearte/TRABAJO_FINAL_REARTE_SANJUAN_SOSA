from django.urls import path
from home import views

app_name='home'
urlpatterns = [
    path('', views.home, name='index'),
    path('about_me/', views.about_me, name="home_about_me"),
    path('blog/',views.blog, name="blog"),
    path('search', views.search, name='search'),
]