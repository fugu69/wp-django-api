from django.urls import path
from .views import (
    PlayerDetailView,
    PlayerPlayerUpdateView, 
    player_detail_html, 
    ArticleListView, 
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

    # Player Udate info
    path('player/<int:pk>/edit/', PlayerPlayerUpdateView.as_view(), name='player_update'),
]
