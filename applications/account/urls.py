from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.account.views import (
    RegisterAPIView, ChangePasswordAPIView, ActivationAPIView,
    ForgotPasswordAPIView, ForgotPasswordCompleteAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="account_register"),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('change_password/', ChangePasswordAPIView.as_view(), name="account_change_password"),
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view(), name="account_forgot_password"),
    path('forgot_password_complete/', ForgotPasswordCompleteAPIView.as_view(), name="account_complete_password")
]