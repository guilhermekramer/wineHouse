from rest_framework import serializers
from apiWine.models.favoriteModel import Favorite
from apiWine.serializers.userSerializer import UserSerializer
from apiWine.serializers.wineSerializer import WineSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    wine = WineSerializer()
    user = UserSerializer()

    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = "__all__"




 

 