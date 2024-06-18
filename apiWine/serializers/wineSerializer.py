from rest_framework import serializers
from apiWine.models.wineModel import Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'
    
    
        