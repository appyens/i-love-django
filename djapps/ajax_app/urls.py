from django.urls import path
from . import views

app_name = 'ajax_app'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('post/postfriend/', views.post_friend, name='post_friend'),
    path('get/validate/nickname/', views.validate_nickname, name='validate_nickname'),
]