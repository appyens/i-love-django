from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'task_one'

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    # path('edit/', views.edit, name='edit'),
    # auth urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),
    # change password urls
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password views
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # user profiles
    # path('users/', views.user_list, name='user_list'),
    # path('users/<str:username>', views.user_detail, name='user_detail'),

]
