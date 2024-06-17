from rest_framework import serializers
from apiWine.models.userModel import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
