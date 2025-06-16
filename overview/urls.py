from django.urls import path
from .views import (
    PlayerDetailView, 
    player_detail_html, 
    ArticleListView, 
    articles_list_view,
    articles_list_view,
    article_create,
    article_update,
    article_delete,
)

urlpatterns = [
    # Player info API response
    path('players/<int:id>/', PlayerDetailView.as_view(), name='player-detail'),

    # HTML rendering
    path('players/<int:id>/view/', player_detail_html, name='player-detail-html'),

    # Article info API response
    path('articles/', ArticleListView.as_view(), name='articles-list'),

    # Article info HTML response
    path('articles/view/', articles_list_view, name='articles-list-view'),

    # Article CRUD
    path('articles/view/', articles_list_view, name='articles-list-view'),
    path('articles/create/', article_create, name='article-create'),
    path('articles/<int:pk>/update/', article_update, name='article-update'),
    path('articles/<int:pk>/delete/', article_delete, name='article-delete'),
]
