from django.urls import path
from .views import LoginView, LogoutView, RegisterView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login', LoginView.as_view(), name='sign_in'),
    path('register', RegisterView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(), name='sign_out'),
    path(
        'reset-password',
        PasswordResetView.as_view(template_name='password_reset.html'),
        name='reset_password'),
    path(
        'reset-password-done',
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path(
        'reset-password/<uidb64>/<token>',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path(
        'reset-password-complete',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
]
