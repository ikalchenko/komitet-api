from rest_framework.serializers import ModelSerializer
import django.contrib.auth.models as auth_models


class TestSerializer(ModelSerializer):

    class Meta:
        model = auth_models.User
        fields = '__all__'
