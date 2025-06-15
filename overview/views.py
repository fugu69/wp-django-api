from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import PlayerPlayer, ArticleArticle
from .serializers import PlayerSerializer, ArticleSerializer

# Player info
class PlayerDetailView(generics.RetrieveAPIView):
    queryset = PlayerPlayer.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'id'

def player_detail_html(request, id):
    player = get_object_or_404(PlayerPlayer, id=id)
    return render(request, 'overview/player_detail.html', {'player': player})

# Articles info
class ArticleListView(generics.ListAPIView):
    queryset = ArticleArticle.objects.all()
    serializer_class = ArticleSerializer

def articles_list_view(request):
    articles = ArticleArticle.objects.all()[:10]  # first 10 articles
    return render(request, 'overview/articles_list.html', {'articles': articles})