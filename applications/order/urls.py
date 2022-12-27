from django.urls import path, include
from applications.order.views import OrderApiView, OrderConfirmApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderApiView)

urlpatterns = [
<<<<<<< HEAD
=======
    path('confirm/<uuid:code>/', OrderConfirmApiView.as_view()),
>>>>>>> d47deb2b96fe9c24981f24f944a60efa14bf1a40
    path('', include(router.urls))
]