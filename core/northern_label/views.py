from django.shortcuts import render
from northern_label.models import Category
from rest_framework import generics
from northern_label.serializers import CategorySerializer

class CategoryAPIView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

