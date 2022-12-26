from django.urls import path, include
from applications.order.views import OrderApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(OrderApiView)

urlpatterns = [
    path('order/', include(router.urls))
]