import logging
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from applications.feedback import services
from applications.feedback.serializsers import FanSerializer, RatingSerializer, Rating


like_logger = logging.getLogger('LIKE')

class LikedMixin:
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        obj = self.get_object()
        services.add_like(obj, request.user)
        status = 'liked'
        
        like_logger.info("User liked product")
        return Response({'status': status})

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        services.remove_like(obj, request.user)
        status = 'unliked'

        like_logger.info("User unliked product")
        return Response({'status': status})

    @action(detail=True, methods=['get'])
    def get_fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)

        like_logger.info("User browsing fans")
        return Response(serializer.data)
    
class RatingMixin:
    @action(detail=True, methods=['post'])
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    @action(detail=True, methods=['put', 'patch'])
    def rating_update(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['delete'])
    def rating_delete(self, request, pk, *args, **kwargs):
        rating_obj, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        rating_obj.delete()
        
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
        
    
        
        