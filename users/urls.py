from django.urls import path
from .views import SignUpView, UserListView, ActivateUserView, ResetPasswordView, ResetPasswordRequestView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.SimpleRouter()

app_name = 'users'
urlpatterns = [
    path('auth/signup', SignUpView.as_view(), name='sign-up'),
    path('users', UserListView.as_view(), name='user-list'),
    path('auth/login', obtain_jwt_token),
    path('auth/verify', verify_jwt_token),
    path('auth/refresh', verify_jwt_token),
    path('auth/activate/<str:uidb64>/<str:token>',
         ActivateUserView.as_view(),
         name='activate'),
    path('auth/reset-password', ResetPasswordRequestView.as_view(),
         name='reset-password-request'),
    path('auth/reset-password/<str:uidb64>/<str:token>',
         ResetPasswordView.as_view(),
         name='reset-password'),
] + router.urls
