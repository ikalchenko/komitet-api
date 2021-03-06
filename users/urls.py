from django.urls import path
from .views import SignUpView, ActivateUserView, ResetPasswordView, ResetPasswordRequestView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from .views import UsersInKomitetView

app_name = 'users'
urlpatterns = [
    path('auth/signup', SignUpView.as_view(), name='sign-up'),
    path('auth/login', obtain_jwt_token),
    path('auth/verify', verify_jwt_token),
    path('auth/refresh', refresh_jwt_token),
    path('auth/activate/<str:uidb64>/<str:token>',
         ActivateUserView.as_view(),
         name='activate'),
    path('auth/reset-password', ResetPasswordRequestView.as_view(),
         name='reset-password-request'),
    path('auth/reset-password/<str:uidb64>/<str:token>',
         ResetPasswordView.as_view(),
         name='reset-password'),
    path('komitets/<int:komitet_id>/users', UsersInKomitetView.as_view(),
         name='users-in-komitet'),
]
