from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from applications.product.permissions import IsProductOwnerOrReadOnly
from core.viewsets.product_viewsets import ModelViewSet
from applications.feedback.mixins import LikedMixin, RatingMixin
from rest_framework.decorators import action
from rest_framework.response import Response


class ProductViewSet(LikedMixin, RatingMixin, ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsProductOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name']
    order_fields = ['price']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    @action(detail=True, methods=['GET'])
    def recommend(self, request, pk=None):
        category = self.get_object().category
        queryset = Product.objects.filter(category=category)
        serializers = ProductSerializer(queryset, many=True)
        return Response(serializers.data)

