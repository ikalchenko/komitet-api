from rest_framework import serializers
import json
from komitets.models import Komitet


class KomitetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Komitet
        fields = ('id', 'title', 'description', 'image', 'background')
