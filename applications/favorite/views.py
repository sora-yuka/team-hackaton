from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from applications.favorite.serializers import FavoriteSerializer
from applications.favorite.models import Favorite
from applications.favorite.permissions import IsFavoriteOwnerOrReadOnly

class FavoriteViewSet(ModelViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    permission_classes = [IsFavoriteOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset