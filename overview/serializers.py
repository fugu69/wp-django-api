from rest_framework import serializers
from .models import PlayerPlayer

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPlayer
        fields = '__all__'
