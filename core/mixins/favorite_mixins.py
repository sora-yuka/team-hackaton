"""
Basic building blocks for generic class based views.

We don't bind behaviour to http method handlers yet,
which allows mixin classes to be composed in interesting ways.
"""
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

logger = logging.getLogger('FAVORITE')

class CreateModelMixin:
    """
    Create a model instance.
    """
    @method_decorator(cache_page(60))
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info("User added product to favorite")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ListModelMixin:
    """
    List a queryset.
    """
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        logger.info("User browsing favorite list")
        return Response(serializer.data)


class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """
    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        logger.info("User browsing favorite list in detail")
        return Response(serializer.data)


class DestroyModelMixin:
    """
    Destroy a model instance.
    """
    @method_decorator(cache_page(60))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        logger.info("User removed favorite from list")
        return Response('Post deleted successfully',status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()