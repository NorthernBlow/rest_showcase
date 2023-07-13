from django.shortcuts import render
from northern_label.models import Category, Brand, Product
from rest_framework import generics, viewsets
from northern_label.serializers import CategorySerializer, BrandSerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination




class CategoryAPIView(generics.ListAPIView):
    """
    A simple set for viewing all categories
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class BrandAPIView(generics.ListAPIView):
    """
    A simple set for viewing all brands
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = None



class ProductAPIView(generics.ListAPIView):
    """
    set to view all products
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer



