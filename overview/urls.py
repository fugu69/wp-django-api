from django.urls import path
from .views import (
    PlayerDetailView,
    PlayerPlayerUpdateView, 
    player_detail_html, 
    ArticleDetailView,
    ArticleListView,
    article_detail_html,
    article_update
)

urlpatterns = [
    # Player info API response
    path('players/<int:id>/', PlayerDetailView.as_view(), name='player-detail'),

    # Player HTML rendering
    path('players/<int:id>/view/', player_detail_html, name='player-detail-html'),

    # Player Update info
    path('players/<int:pk>/edit/', PlayerPlayerUpdateView.as_view(), name='player_update'),

    # Article API detail
    path('articles/<int:id>/', ArticleDetailView.as_view(), name='article-detail'),

    # Article HTML detail
    path('articles/<int:id>/view/', article_detail_html, name='article-detail-html'),

     # Article Update form (HTML)
    path('articles/<int:id>/edit/', article_update, name='article-update'),

    # Article list API view
    path('articles/', ArticleListView.as_view(), name='article-list'),
]


