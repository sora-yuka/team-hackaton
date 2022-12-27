from rest_framework.decorators import action
from rest_framework.response import Response
from applications.feedback import services
from applications.feedback.serializers import FanSerializer


class LikedMixin:
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        obj = self.get_object()
        services.add_like(obj, request.user)

        return Response()

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        services.remove_like(obj, request.user)

        return Response()

    @action(detail=True, methods=['get'])
    def get_fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)

        return Response(serializer.data)