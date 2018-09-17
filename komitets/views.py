from django.shortcuts import render
from rest_framework import views, status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import KomitetSerializer
from .models import Komitet


class CreateKomitetView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KomitetSerializer

    def get_queryset(self):
        return Komitet.objects.users_komitets(self.request.user)


class KomitetDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KomitetSerializer
    queryset = Komitet.objects.all()
