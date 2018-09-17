from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import KomitetSerializer
from users.serializers import UserPermissionsSerializer
from .models import Komitet
from users.models import UserPermissions
from django.contrib.auth.models import User


class CreateKomitetView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KomitetSerializer

    def get_queryset(self):
        return Komitet.objects.users_komitets(self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = KomitetSerializer(data=request.POST)
        if serializer.is_valid():
            komitet = Komitet(
                title=request.POST.get('title', ''),
                description=request.POST.get('description', ''),
                image=request.POST.get('image', ''),
                background=request.POST.get('background', ''),
            )
            komitet.save()
            komitet.refresh_from_db()
            UserPermissions.objects.create(
                user=request.user,
                komitet=komitet,
                permission='A'
            )
            serializer = KomitetSerializer(data=komitet)
            serializer.is_valid()
            return Response(serializer.data)


class KomitetDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KomitetSerializer
    queryset = Komitet.objects.all()


class AddUsersToKomitetView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPermissionsSerializer

    def get_queryset(self):
        return Komitet.objects.users_komitets(self.request.user)
