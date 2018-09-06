from django.urls import path
from .views import TestViewSet

urlpatterns = [
    path('test', TestViewSet.as_view({'get': 'list'}))
]
