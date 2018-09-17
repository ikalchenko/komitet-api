from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('komitets.urls')),
    # path('api/', include('auth.urls')),
    # path('api/', include('cards.urls')),
]
