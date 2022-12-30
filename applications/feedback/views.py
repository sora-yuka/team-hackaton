from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.viewsets.comment_viewsets import ModelViewSet
from applications.feedback.models import Comment
from applications.feedback.serializsers import CommentSerializer


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
