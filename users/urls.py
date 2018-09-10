from django.urls import path
from .views import TestViewSet, SignUpView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('test', TestViewSet)

urlpatterns = [
    path('sign-up', SignUpView, name='sign-up')
    # path('activate/<str:uidb64>/<str:token>',
    #      views.ActivateUserView.as_view(),
    #      name='activate'),
    # path('reset-password',
    #      views.ResetPasswordRequestView.as_view(),
    #      name='reset-password-request'),
    # path('reset-password/<str:uidb64>/<str:token>',
    #      views.ResetPasswordView.as_view(),
    #      name='reset-password'),
] + router.urls
