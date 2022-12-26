from django.urls import path, include
from applications.product.views import (
    ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView, 
    ProductUpdateAPIView, ProductDestroyAPIView
)

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('post/', ProductCreateAPIView.as_view()),
    path('<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('edit/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', ProductDestroyAPIView.as_view()),
]