from django.urls import path
from .views import PlayerDetailView, player_detail_html

urlpatterns = [
    # API response
    path('players/<int:id>/', PlayerDetailView.as_view(), name='player-detail'),

    # HTML rendering
    path('players/<int:id>/view/', player_detail_html, name='player-detail-html'),
]
