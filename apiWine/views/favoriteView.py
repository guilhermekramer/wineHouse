from rest_framework import viewsets
from apiWine.models.favoriteModel import Favorite
from apiWine.serializers.favoriteSerializer import FavoriteCreateSerializer, FavoriteSerializer


class FavortieViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return FavoriteCreateSerializer
        return FavoriteSerializer

    
