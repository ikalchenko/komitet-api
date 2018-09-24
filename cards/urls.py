from django.urls import path
from .views import CreateCardView


app_name = 'cards'
urlpatterns = [
    path('komitets/<int:komitet_id>/cards',
         CreateCardView.as_view(), name='create-card')
]
