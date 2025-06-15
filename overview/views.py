from rest_framework import generics
from .models import PlayerPlayer
from .serializers import PlayerSerializer

class PlayerDetailView(generics.RetrieveAPIView):
    queryset = PlayerPlayer.objects.all()
    serializer_class = PlayerSerializer

