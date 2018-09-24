from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .serializers import CardSerializer
from .models import Card
from komitets.models import Komitet


class CreateCardView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_serializer(self, *args, **kwargs):
        try:
            komitet = Komitet.objects.get(pk=self.kwargs['komitet_id'])
        except Komitet.DoesNotExist:
            raise NotFound
        if self.request.user in komitet.get_writers() and self.request.method == 'POST':
            return CardSerializer(data=self.request.POST, context={
                'komitet': self.kwargs['komitet_id'],
                'request': self.request
            })
        elif self.request.user in komitet.get_not_banned() and self.request.method == 'GET':
            return CardSerializer(self.get_queryset(), many=True)

    def get_queryset(self):
        return Card.objects.filter(komitet=self.kwargs['komitet_id'])
