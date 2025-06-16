from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views.generic import UpdateView
from rest_framework import generics
from .models import PlayerPlayer, ArticleArticle
from .serializers import PlayerSerializer, ArticleSerializer
from .forms import PlayerPlayerUpdateForm

# Player info
class PlayerDetailView(generics.RetrieveAPIView):
    queryset = PlayerPlayer.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'id'

def player_detail_html(request, id):
    player = get_object_or_404(PlayerPlayer, id=id)
    return render(request, 'overview/player_detail.html', {'player': player})

# Player update
class PlayerPlayerUpdateView(UpdateView):
    model = PlayerPlayer
    form_class = PlayerPlayerUpdateForm
    template_name = 'overview/player_update.html'
    
    def get_success_url(self):
        return reverse('player-detail-html', kwargs={'id': self.object.pk})

#Articles info
# API View
# class ArticleListView(generics.ListAPIView):
#     queryset = ArticleArticle.objects.all()
#     serializer_class = ArticleSerializer

# HTML View
def article_detail_html(request, id):
    article = get_object_or_404(ArticleArticle, id=id)
    return render(request, 'overview/article_detail.html', {'article': article})

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = ArticleArticle.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'

