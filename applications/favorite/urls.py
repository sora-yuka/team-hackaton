from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.favorite.views import FavoriteViewSet

router = DefaultRouter()
router.register('favorites/', FavoriteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
