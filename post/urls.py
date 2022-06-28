from django.urls import path
from . import views


app_name='post'
urlpatterns = [
    path('form_post/', views.form_post, name='form_post'),
    path('detalle_post/<int:pk>/comment/', views.form_comment, name='form_comment'),
    path('detalle_post/<int:pk>', views.detallePost, name='detalle_post'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
    path('delete_post/<int:pk>', views.deletePost, name='delete_post'),
    path('error',views.error, name='error')
]