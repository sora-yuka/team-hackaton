import logging
from core.viewsets.order_viwsets import ModelViewSet, GenericViewSet
from applications.order.permissions import IsOrderOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from core.mixins import order_mixins

from applications.order.models import Order
from applications.order.serializers import OrderSerializer

logger = logging.getLogger('ORDER')

class OrderApiView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOrderOwner]
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['product']
    ordering_fields = ['id']
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user.id)
        return queryset
    
    
class OrderListApiView(order_mixins.ListModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOrderOwner]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_confirm=True)
        return queryset
    
    
class OrderConfirmApiView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Order, activation_code=code)
        
        if order.amount > order.product.amount:
            return Response(f'Sorry, but right now we dont have so much pcs')
        
        if not order.is_confirm:
            order.is_confirm = True
            order.status = 'in_processing'
            
            order.product.amount -= order.amount
            order.product.save(update_fields=['amount'])
            order.save(update_fields=['is_confirm', 'status', 'product'])
            logger.info("User confirmed order")
            return Response({'message': 'You have confirmed order'}, status=status.HTTP_200_OK)
        logger.info("User already confirmed order")
        return Response({'message': 'You have already confirmed order'}, status=status.HTTP_400_BAD_REQUEST)