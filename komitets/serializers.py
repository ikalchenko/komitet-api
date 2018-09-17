from rest_framework import serializers
import json
from komitets.models import Komitet
from users.models import UserPermissions
from users.serializers import UserSerializer


class KomitetSerializer(serializers.ModelSerializer):
    # members = UserSerializer()

    class Meta:
        model = Komitet
        fields = ('id', 'title', 'description', 'image', 'background', 'members')

    def create(self, validated_data):
        komitet = Komitet(
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
            image=validated_data.get('image', ''),
            background=validated_data.get('background', ''),
        )
        komitet.save()
        komitet.refresh_from_db()
        UserPermissions.objects.create(
            user=self.context['request'].user,
            komitet=komitet,
            permission='A'
        )
        return komitet
