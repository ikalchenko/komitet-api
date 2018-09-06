from django.shortcuts import render

from rest_framework import viewsets

import django.contrib.auth.models as auth_models
from .serializers import TestSerializer
# Create your views here.


class TestViewSet(viewsets.ModelViewSet):
    model = auth_models.User
    queryset = auth_models.User.objects.all()
    serializer_class = TestSerializer
