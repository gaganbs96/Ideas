import datetime
import calendar

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.db import transaction

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework import generics, filters
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action, api_view, parser_classes
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializer import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super(ReviewViewSet, self).create(request, *args, **kwargs)
        return response


    def list(self, request, *args, **kwargs):
        return super(ReviewViewSet, self).list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super(ReviewViewSet, self).destroy(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super(ReviewViewSet, self).retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     return super(ReviewViewSet, self).update(request, *args, **kwargs)




