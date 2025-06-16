from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import PlayerPlayer, ArticleArticle
from .serializers import PlayerSerializer, ArticleSerializer
from .forms import ArticleForm

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

# Article CRUD
# Fetch articles 1-10
def articles_list_view(request):
    articles = ArticleArticle.objects.all()[:10]  # first 10 articles
    return render(request, 'overview/articles_list.html', {'articles': articles})

# Create - POST
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles-list-view')
    else:
        form = ArticleForm()
    return render(request, 'overview/article_form.html', {'form': form})

# Update - POST
def article_update(request, pk):
    article = get_object_or_404(ArticleArticle, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles-list-view')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'overview/article_form.html', {'form': form})

# Delete - DELETE
def article_delete(request, pk):
    article = get_object_or_404(ArticleArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles-list-view')
    return render(request, 'overview/article_confirm_delete.html', {'article': article})