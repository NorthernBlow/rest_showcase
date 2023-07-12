from rest_framework import serializers
from northern_label.models import Category

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('name', 'description')
