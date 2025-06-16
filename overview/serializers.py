from rest_framework import serializers
from .models import PlayerPlayer, ArticleArticle

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPlayer
        fields = ['id', 'image', 'energy', 'gold', 'time_zone']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleArticle
        fields = ['title', 'body']
