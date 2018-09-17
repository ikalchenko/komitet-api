from django.urls import path
from .views import CreateKomitetView, KomitetDetailView, UsersInKomitetView


app_name = 'komitets'
urlpatterns = [
    path('komitets', CreateKomitetView.as_view(), name='create-komitet'),
    path('komitets/<int:pk>', KomitetDetailView.as_view(), name='komitet-detail'),
    path('komitets/<int:pk>/users', UsersInKomitetView.as_view(),
         name='users-in-komitet'),
]
