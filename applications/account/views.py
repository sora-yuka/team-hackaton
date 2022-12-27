from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
import logging

from applications.account.serializers import (
    RegisterSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, 
    ForgotPasswordCompleteSerializer
)

logger = logging.getLogger('ACCOUNT')
User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info('User signed up')
        return Response('You have successfully registred.\n '
                        'We sent an activation email',
                        status=201
                        )


class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        logger.info('User changed password')
        return Response('Password updated successfully...')


class ActivationAPIView(APIView):
    def get(self, request, activation_code):
        try:
            logger.info('User activated profile')
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message': 'successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            logger.warning('ActivationAPIView code doesnt work or was acitavated')
            return Response({'message': 'Wrong email!'}, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        logger.info('User forgot password')
        return Response('We have sent an email to reset your password...')


class ForgotPasswordCompleteAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        logger.info('User regained access to the profile')
        return Response('Password updadted successfully!')