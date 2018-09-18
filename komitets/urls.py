from django.urls import path
from .views import CreateKomitetView, KomitetDetailView


app_name = 'komitets'
urlpatterns = [
    path('komitets', CreateKomitetView.as_view(), name='create-komitet'),
    path('komitets/<int:pk>', KomitetDetailView.as_view(), name='komitet-detail'),

]
