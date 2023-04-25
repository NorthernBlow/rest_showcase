from django.shortcuts import render
from northern_label.models import Artists
from rest_framework import generics
from northern_label.serializers import ArtistsSerializer

class ArtistsAPIView(generics.ListAPIView):
	queryset = Artists.objects.all()
	serializer_class = ArtistsSerializer

