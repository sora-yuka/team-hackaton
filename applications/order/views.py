from rest_framework.viewsets import ModelViewSet
from applications.order.permissions import IsOrderOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404

from applications.order.models import Order
from applications.order.serializers import OrderSerializer

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
        queryset = queryset.filter(owner=self.request.user)
        return queryset
    
    
class OrderConfirmApiView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Order, activation_code=code)
        
        if not order.is_confirm:
            order.is_confirm = True
            order.status = 'in_processing'
            
            order.product.amount -= order.amount
            order.product.save(update_fields=['amount'])
            order.save(update_fields=['is_confirm', 'status', 'product'])
            return Response({'message': 'You have confirmed order'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already confirmed order'}, status=status.HTTP_400_BAD_REQUEST)
    