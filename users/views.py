from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .tokens import account_activation_token as aat
from .tokens import password_reset_token as prt
from .utils import send_confirmation_email


class SignUpView(views.APIView):
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


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ActivateUserView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user and aat.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            return Response({'status': 'succes'}, status.HTTP_200_OK)
        return Response({'status': 'fail'}, status.HTTP_400_BAD_REQUEST)
