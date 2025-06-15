from rest_framework import serializers
from .models import PlayerPlayer

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPlayer
        fields = ['id', 'image', 'energy', 'gold', 'time_zone']
