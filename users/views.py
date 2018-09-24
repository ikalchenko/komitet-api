from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .serializers import UserSerializer
from .tokens import account_activation_token as aat
from .tokens import password_reset_token as prt
from .utils import send_confirmation_email
from .serializers import UserPermissionsSerializer
from komitets.models import Komitet
from rest_framework.exceptions import NotFound
from users.models import UserPermissions


class SignUpView(views.APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(first_name=serializer.validated_data['first_name'],
                                            last_name=serializer.validated_data['last_name'],
                                            username=serializer.validated_data['username'],
                                            email=serializer.validated_data['email'],
                                            password=serializer.validated_data['password'],
                                            is_active=False)
            send_confirmation_email(self.request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivateUserView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user and aat.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            return Response({}, status.HTTP_200_OK)
        return Response({}, status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user and prt.check_token(user, kwargs['token']):
            user.set_password(self.request.POST['new_password'])
            user.save()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        return Response({'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordRequestView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        if user:
            send_confirmation_email(
                self.request, user, reset_password=True)
        return Response({'status': 'success'}, status.HTTP_200_OK)


class UsersInKomitetView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'POST':
            return UserPermissionsSerializer(data=self.request.POST, context={
                'komitet': self.kwargs['komitet_id'],
                'request': self.request
            })
        elif self.request.method == 'GET':
            return UserPermissionsSerializer(self.get_queryset(), many=True)

    def get_queryset(self):
        return UserPermissions.objects.filter(komitet=self.kwargs['komitet_id'])
