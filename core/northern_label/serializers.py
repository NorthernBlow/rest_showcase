from rest_framework import serializers
from northern_label.models import Category, Brand, Product




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'category']



class CategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True, read_only=True)
	
    class Meta:
        model = Category
        fields = ['name', 'slug', 'photo', 'brands']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
