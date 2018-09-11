from django.urls import path
from .views import SignUpView, UserListView, ActivateUserView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.SimpleRouter()

app_name = 'users'
urlpatterns = [
    path('signup', SignUpView.as_view(), name='sign-up'),
    path('users', UserListView.as_view(), name='user-list'),
    path('login', obtain_jwt_token),
    path('activate/<str:uidb64>/<str:token>',
         ActivateUserView.as_view(),
         name='activate'),
    # path('reset-password/<str:uidb64>/<str:token>',
    #      views.ResetPasswordView.as_view(),
    #      name='reset-password'),
] + router.urls
