from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from komitets.models import Komitet
from .models import UserPermissions


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name')


class UserPermissionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPermissions
        fields = ('user', 'komitet', 'permission')

    def create(self, validated_data):
        # check for existance of this permission
        user = self.context['request'].user
        komitet = self.context['komitet']
        komitet = Komitet.objects.get(
            pk=komitet
        )
        if user in komitet.get_writers():
            user_permission = UserPermissions(
                user=validated_data['user'],
                komitet=komitet,
                permission=validated_data['permission']
            )
            user_permission.save()
        return user_permission
