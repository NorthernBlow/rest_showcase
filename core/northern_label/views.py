from django.shortcuts import render
from northern_label.models import Category, Brand, Product
from rest_framework import generics, viewsets
from northern_label.serializers import CategorySerializer, BrandSerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser



class CategoryAPIView(generics.ListAPIView):
    """
    A simple set for viewing all categories
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

