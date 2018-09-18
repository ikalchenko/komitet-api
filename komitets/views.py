from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import KomitetSerializer
from users.serializers import UserPermissionsSerializer
from .models import Komitet
from users.models import UserPermissions
from rest_framework.exceptions import NotFound, PermissionDenied
from django.contrib.auth.models import User


class CreateKomitetView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KomitetSerializer

    def get_queryset(self):
        return Komitet.objects.users_komitets(self.request.user)


class KomitetDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KomitetSerializer
    queryset = Komitet.objects.all()

    def get_object(self):
        try:
            komitet = Komitet.objects.get(pk=self.kwargs['pk'])
        except Komitet.DoesNotExist:
            raise NotFound
        if self.request.user in komitet.get_not_banned():
            return komitet
        raise PermissionDenied
