from apiWine.models.userModel import User
from apiWine.serializers.userSerializer import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
     

    queryset = User.objects.all()
    serializer_class = UserSerializer


    