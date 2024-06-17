from apiWine.models.userModel import User
from apiWine.serializers.userSerializer import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
