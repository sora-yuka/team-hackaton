from os import path

from rest_framework.routers import DefaultRouter
from django.urls import include

from applications.feedback.views import CommentAPIView, LikeAPIView

router = DefaultRouter()
router.register('comment', CommentAPIView)
router.register('like', LikeAPIView)
router.register('favorite', )



urlpatterns = []
urlpatterns += router.urls