from rest_framework import serializers
from .models import Card
from komitets.models import Komitet
from rest_framework.exceptions import NotFound


class CardSerializer(serializers.ModelSerializer):
    komitet = serializers.CharField(required=False)
    user = serializers.CharField(required=False)
    class Meta:
        model = Card
        fields = '__all__'

    def create(self, validated_data):
        try:
            komitet = Komitet.objects.get(pk=self.context['komitet'])
        except Komitet.DoesNotExist:
            raise NotFound
        card = Card(title=validated_data['title'],
                    text=validated_data['text'],
                    type=validated_data['type'],
                    komitet=komitet,
                    user=self.context['request'].user)
        card.save()
        return card
