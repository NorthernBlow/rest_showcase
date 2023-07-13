from django.shortcuts import render
from rest_framework import pagination
from rest_framework.response import responses
from rest_framework.routers import Response
from northern_label.models import Category, Brand, Product
from rest_framework import generics, viewsets
from northern_label.serializers import CategorySerializer, BrandSerializer, ProductSerializer, CategoryPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema




class CategoryAPIView(generics.ListAPIView):
    """
    A simple set for viewing all categories
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class BrandAPIView(generics.ListAPIView):
    """
    A simple set for viewing all brands
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = CategoryPagination



class ProductViewSet(viewsets.ViewSet):
    """
    Viewset to view all products
    """

    queryset = Product.objects.all()
    pagination_class = CategoryPagination

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)



