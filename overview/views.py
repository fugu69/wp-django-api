from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView
from rest_framework import generics
from .models import PlayerPlayer, ArticleArticle
from .serializers import PlayerSerializer, ArticleSerializer
from .forms import ArticleForm, PlayerPlayerUpdateForm

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

# Articles info
class ArticleListView(generics.ListAPIView):
    queryset = ArticleArticle.objects.all()
    serializer_class = ArticleSerializer

